""" API for machine learning
"""
import pickle
import joblib
from flask import Flask, request, jsonify


# load model
CV = pickle.load(open("models/vector.pickel", "rb"))
MODEL = open('models/NB_spam_model.pkl', 'rb')
CLF = joblib.load(MODEL)
REPORT = "This is SMS spam detection model. Use the format {'message': 'SMS message'} and POST to get prediction."  # pylint: disable=line-too-long

# app
APP = Flask(__name__)


@APP.route('/', methods=['GET'])
def home():
    """
    GET Request
    """
    # Give message to user
    return {"message": REPORT}


@APP.route('/', methods=['POST'])
def predict():
    """
    POST Request
    """
    # get data
    data = request.get_json(force=True)
    data = data['message']
    data = [data]
    # convert data into array
    vect = CV.transform(data).toarray()

    # predictions
    my_prediction = CLF.predict(vect)

    # check predicted value
    if my_prediction[0] == 0:
        response = "This is not a spam, It is a ham"
    elif my_prediction[0] == 1:
        response = "This is a spam"

    # return data
    return jsonify(results=response)


if __name__ == '__main__':
    APP.run(port=5000, debug=True)
