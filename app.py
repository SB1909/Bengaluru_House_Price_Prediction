import pickle
import json
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy as np
import pandas as pd

app = Flask(__name__)
# Loading Model
model=pickle.load(open('Bengaluru_House_Price_model.pickle', 'rb'))
columns = json.load(open("columns.json",'rb'))["data_columns"]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['GET','POST'])
def predict_api():
    #data = request.json['data']
    #print(data)
    #new_data = np.array(list(data.values())).reshape(1,-1)
    #new_data = pd.DataFrame([list(data.values())], columns = columns)[0]
    #output = model.predict(new_data)[0]

    area_type = request.form['area_type']
    location = request.form['location']
    bhk = int(request.form['bhk'])
    total_sqft = float(request.form['total_sqft'])
    
    output = model.predict(pd.DataFrame([[area_type, location, bhk, total_sqft]], columns = columns))[0]

    return jsonify(float(output))

if __name__=='__main__':
    app.run(debug = True)