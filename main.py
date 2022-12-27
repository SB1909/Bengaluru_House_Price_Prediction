import pickle
import json
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
# Loading Model
model=pickle.load(open('Bengaluru_House_Price_model.pickle', 'rb'))
columns = json.load(open("columns.json",'rb'))["data_columns"]
locations = json.load(open("locations.json",'rb'))["locations"]
area_type = json.load(open("area_type.json",'rb'))["area_type"]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['GET','POST'])
def predict_api():
    area_type = request.form['area_type']
    location = request.form['uiLocations']
    bhk = int(request.form['bhk'])
    total_sqft = float(request.form['total_sqft'])
    output = model.predict(pd.DataFrame([[area_type, location, bhk, total_sqft]], columns = columns))[0]
    return jsonify(float(output))

@ app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': locations
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@ app.route('/predict', methods=['POST'])
def predict():
    area_type = request.form['area_type']
    location = request.form['uiLocations']
    bhk = int(request.form['bhk'])
    total_sqft = float(request.form['total_sqft'])
    
    output = model.predict(pd.DataFrame([[area_type, location, bhk, total_sqft]], columns = columns))[0]

    price = round(float(output),2)
    
    return render_template('home.html', prediction_text = "The predicted house price is ₹ {} lakhs.".format(price))

if __name__=='__main__':
    app.run(debug = True)