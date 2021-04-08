from flask import Flask, request, jsonify, render_template
import json
import pickle
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_predicted_price(location, sqft, bath, bhk):
    try:
        index_location = __data_columns.index(location.lower())
    except:
        index_location = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if index_location >= 0:
        x[index_location] = 1

    return round(__model.predict([x])[0], 2)

def get_location_util():
    return __locations

def load_saved_artifacts():
    print("Loading saved artifacts...")
    global __data_columns
    global __locations
    global __model

    with open("./artifacts/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]

    with open("./artifacts/house_price_prediction_system.pickle", 'rb') as f:
        __model = pickle.load(f)

    print("..done")


app = Flask(__name__, template_folder='')

@app.route('/')
def home():
    return render_template('app.html')

@app.route("/get_location")
def get_location():
    response = jsonify({
        'locations' : get_location_util()
    })
    response.headers.add('Access-Control-Allow-Origin','https://house-price-prediction-system7.herokuapp.com/')

    return response

@app.route('/predict_house_price', methods=['POST'])
def predict_house_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'predicted_price' : get_predicted_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin','https://house-price-prediction-system7.herokuapp.com/')

    return response


if __name__ == "__main__":
    print("Starting Python Flask server for House price prediction system")
    load_saved_artifacts()
    get_location_util()
    app.run(debug=True)
