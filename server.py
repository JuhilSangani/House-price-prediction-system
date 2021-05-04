from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__, template_folder='')

@app.route('/')
def home():
    return render_template('app.html')

@app.route("/get_location")
def get_location():
    response = jsonify({
        'locations' : util.get_location()
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response

@app.route('/predict_house_price', methods=['POST'])
def predict_house_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'predicted_price' : util.get_predicted_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin','*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask server for House price prediction system")
    util.load_saved_artifacts()
    app.run()
