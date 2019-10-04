from flask import Flask, render_template, url_for, request, jsonify
import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

# load model
cv = pickle.load(open("models/vector.pickel", "rb"))
NB_spam_model = open('models/NB_spam_model.pkl', 'rb')
clf = joblib.load(NB_spam_model)

# app
app = Flask(__name__)

# routes


@app.route('/', methods=['GET'])
def home():
    # Give message to user
    return {"message": "This is SMS spam detection model. Use the format {'message': 'SMS message'} and POST to get prediction."}


@app.route('/', methods=['POST'])
def predict():
    # get data
    data = request.get_json(force=True)
    data = data['message']
    data = [data]
    # convert data into array
    vect = cv.transform(data).toarray()

    # predictions
    my_prediction = clf.predict(vect)

    # check predicted value
    if my_prediction[0] == 0:
        response = "This is not a spam, It is a ham"
    elif my_prediction[0] == 1:
        response = "This is a spam"

    # return data
    return jsonify(results=response)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
