from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FlightOffer(db.Model):
    __tablename__ = 'flight_offers'
    
    id = db.Column(db.Integer, primary_key=True)
    source = db.Column(db.String(20))
    instant_ticketing_required = db.Column(db.Boolean)
    non_homogeneous = db.Column(db.Boolean)
    one_way = db.Column(db.Boolean)
    last_ticketing_date = db.Column(db.String(10))
    number_of_bookable_seats = db.Column(db.Integer)
    price_id = db.Column(db.Integer, db.ForeignKey('prices.id'))
    
    itineraries = db.relationship('Itinerary', backref='flight_offer', lazy=True)
    traveler_pricings = db.relationship('TravelerPricing', backref='flight_offer', lazy=True)

class Itinerary(db.Model):
    __tablename__ = 'itineraries'
    
    id = db.Column(db.Integer, primary_key=True)
    flight_offer_id = db.Column(db.Integer, db.ForeignKey('flight_offers.id'))
    duration = db.Column(db.String(20))
    
    segments = db.relationship('Segment', backref='itinerary', lazy=True)

class Segment(db.Model):
    __tablename__ = 'segments'
    
    id = db.Column(db.Integer, primary_key=True)
    itinerary_id = db.Column(db.Integer, db.ForeignKey('itineraries.id'))
    departure_iata_code = db.Column(db.String(3))
    departure_terminal = db.Column(db.String(10))
    departure_at = db.Column(db.String(25))
    arrival_iata_code = db.Column(db.String(3))
    arrival_terminal = db.Column(db.String(10), nullable=True)
    arrival_at = db.Column(db.String(25))
    carrier_code = db.Column(db.String(10))
    flight_number = db.Column(db.String(10))
    aircraft_code = db.Column(db.String(10))
    operating_carrier_code = db.Column(db.String(10))
    duration = db.Column(db.String(20))
    number_of_stops = db.Column(db.Integer)
    blacklisted_in_eu = db.Column(db.Boolean)

class Price(db.Model):
    __tablename__ = 'prices'
    
    id = db.Column(db.Integer, primary_key=True)
    currency = db.Column(db.String(3))
    total = db.Column(db.String(10))
    base = db.Column(db.String(10))
    grand_total = db.Column(db.String(10))
    
    fees = db.relationship('Fee', backref='price', lazy=True)

class Fee(db.Model):
    __tablename__ = 'fees'
    
    id = db.Column(db.Integer, primary_key=True)
    price_id = db.Column(db.Integer, db.ForeignKey('prices.id'))
    amount = db.Column(db.String(10))
    fee_type = db.Column(db.String(20))

class TravelerPricing(db.Model):
    __tablename__ = 'traveler_pricings'
    
    id = db.Column(db.Integer, primary_key=True)
    flight_offer_id = db.Column(db.Integer, db.ForeignKey('flight_offers.id'))
    traveler_id = db.Column(db.String(10))
    fare_option = db.Column(db.String(20))
    traveler_type = db.Column(db.String(10))
    price_id = db.Column(db.Integer, db.ForeignKey('prices.id'))
    
    fare_details_by_segment = db.relationship('FareDetails', backref='traveler_pricing', lazy=True)

class FareDetails(db.Model):
    __tablename__ = 'fare_details'
    
    id = db.Column(db.Integer, primary_key=True)
    traveler_pricing_id = db.Column(db.Integer, db.ForeignKey('traveler_pricings.id'))
    segment_id = db.Column(db.String(10))
    cabin = db.Column(db.String(20))
    fare_basis = db.Column(db.String(20))
    fare_class = db.Column(db.String(2))
    included_checked_bags_weight = db.Column(db.Integer)
    included_checked_bags_weight_unit = db.Column(db.String(5))

# To set up the database, you can run db.create_all() after configuring your Flask app.
