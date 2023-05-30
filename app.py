# Importing essential libraries and modules

from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pd
import statistics as st
import requests
import pickle
import io
import torch
from torchvision import transforms
# ==============================================================================================

# -------------------------LOADING THE TRAINED MODELS -----------------------------------------------

# Loading crop recommendation model

crop_recommendation_model_path = 'models/RandomForest.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))


yield_pred_model_path= 'models\Yield-pred-model-final.pkl'
yield_pred_model = pickle.load(
    open(yield_pred_model_path, 'rb'))


# =========================================================================================

# Custom functions for calculations


def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    base_url="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/%22+city_name+%22?key=C4KHAUSYXVKSS2565PV7MDC5T"
    response=requests.get(base_url)
    x = response.json()
    y=x['days']
    temp=[]
    hum=[]
    for days in y:
      temp.append((days['tempmax']+days['tempmin'])/2)
      hum.append(days['humidity'])
    temperature=st.mean(temp)
    temperature=round(((temperature-32)*(5/9)),2)
    humidity=round(st.mean(hum),2)
    return temperature, humidity

    # api_key = config.weather_api_key
    # base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    # response = requests.get(complete_url)
    # x = response.json()

    # if x["cod"] != "404":
    #     y = x["main"]

    #     temperature = round((y["temp"] - 273.15), 2)
    #     humidity = y["humidity"]
    #     return temperature, humidity
    # else:
    #     return None

# ===============================================================================================
# ------------------------------------ FLASK APP -------------------------------------------------


app = Flask(__name__)

# render home page


# @ app.route('/')
# def home():
    # title = 'Harvestify - Home'
    # return render_template('index.html', title=title)

# render crop recommendation form page


# @ app.route('/crop-recommend')
# def crop_recommend():
#     title = 'Harvestify - Crop Recommendation'
#     return render_template('crop.html', title=title)

# # render fertilizer recommendation form page


# @ app.route('/fertilizer')
# def fertilizer_recommendation():
#     title = 'Harvestify - Fertilizer Suggestion'

#     return render_template('fertilizer.html', title=title)

# render disease prediction input page

# ===============================================================================================

# CROP CONNECT pages

# render home page

@ app.route('/')
def land():
    title = 'Crop Connect - Home'
    return render_template('cc-index.html', title=title)

# render crop recommendation page
@ app.route('/crm')
def crm():
    title = 'Crop Connect - CRM'
    return render_template('cc-crop.html', title=title)

# render crop yield prediction page

@ app.route('/cyp')
def cyp():
    title = 'Crop Connect - CYP'
    return render_template('cc-yield.html', title=title)

# render list of crops data page

@ app.route('/data')
def data():
    title = 'Crop Connect - CRM'
    return render_template('cc-data.html', title=title)


# ===============================================================================================

# RENDER PREDICTION PAGES

# render crop recommendation result page

        
# render crop recommendation result page for CROP CONNECT


@ app.route('/cc-crop-predict', methods=['POST'])
def cc_crop_prediction():
    title = 'Crop Connect - Crop Recommendation'

    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])

        # state = request.form.get("stt")
        city = request.form.get("city")

        if weather_fetch(city) != None:
            temperature, humidity = weather_fetch(city)
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = crop_recommendation_model.predict(data)
            final_prediction = my_prediction[0]

            return render_template('cc-crop-result.html', prediction=final_prediction, title=title)

        else:

            return render_template('try_again.html', title=title)        

@ app.route('/yield-prediction', methods=['POST'])
def YieldPred():
 title = 'Crop Connect - Crop Yield Prediction'
 crop_list=["apple", "banana", "blackgram", "coconut",
                                 "coffee", "cotton", "grapes", "jute", "kidneybeans",
                                 "lentil", "maize", "mango", "mothbeans", "mungbean",
                                 "muskmelon", "orange", "papaya", "pigeonpeas",
                                 "pomegranate", "rice", "watermelon"]
 crop=[0]*21
 if request.method == 'POST':
        data=[]
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['pottasium'])
        ph = float(request.form['ph'])
        area = float(request.form['area'])
        rainfall = float(request.form['rainfall'])
        crp=request.form.get("crop")
        crop[crop_list.index(crp)]=1
        city = request.form.get("city")
        if weather_fetch(city) != None:
            temperature, humidity = weather_fetch(city)
            data.append(N)
            data.append(P)
            data.append(K)
            data.append(temperature)
            data.append(humidity)
            data.append(ph)
            data.append(rainfall)
            data.append(area)
            data=data+crop
            final_data = np.array([data])
            my_prediction = yield_pred_model.predict(final_data)
            final_prediction = my_prediction[0]/area

            return render_template('cc-yield-result.html', prediction=final_prediction, title=title)
        else:

            return render_template('try_again.html', title=title) 
# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=False)
