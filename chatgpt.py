from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort
# Import your models so they are registered with SQLAlchemy
from .flightResponseDb import FlightOffer, Itinerary, Segment, Price, Fee, TravelerPricing, FareDetails
    
import openai

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)

# Set up your OpenAI API key
client = openai.OpenAI(api_key='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')

# # Define a route to handle chat requests
# @app.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.json.get('message')
#     if not user_message:
#         return jsonify({"error": "No message provided"}), 400

#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-4",  # or your custom model if available
#             messages=[{"role": "user", "content": user_message}]
#         )
#         chat_response = response['choices'][0]['message']['content']
#         return jsonify({"response": chat_response})
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    
# messages = [ {"role": "system", "content": 
#               "You are a intelligent assistant."} ]

# @app.route('/sec', methods=['POST'])
# def userResp():
#     message = request.json.get('message')
#     if message:
#         messages.append(
#             {"role": "user", "content": message},
#         )
#         chat = client.completions.create(
#             model="curie", messages=messages
#         )
#     reply = chat.choices[0].message.content
#     print(f"ChatGPT: {reply}")
#     messages.append({"role": "assistant", "content": reply})

@app.route('/newway', methods=['POST'])
def userResp():
    completion = client.chat.completions.create(model="gpt-4o-mini", messages=[{"role": "user", "content": "Hello world"}])
    reply = completion.choices[0].message.content
    print(f"ChatGPT: {reply}")
    


if __name__ == '__main__':
    app.run(debug=True)

