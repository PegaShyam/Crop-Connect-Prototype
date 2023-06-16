# Importing essential libraries and modules

from flask import Flask, render_template, request, Markup
import numpy as np
import pandas as pd
import statistics as st
import requests
import pickle
import sys
import io
import torch
import math
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
    base_url="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/%22"+city_name+"%22?key=C4KHAUSYXVKSS2565PV7MDC5T"
    response=requests.get(base_url)
    x = response.json()
    y=x['days']
    temp=[]
    hum=[]
    for days in y:
     temp.append((days['tempmax']+days['tempmin'])/2)
     hum.append(days['humidity'])
    print(len(hum),hum,file=sys.stderr)

    temperature=st.mean(temp)
    temperature=round(((temperature-32)*(5/9)),2)
    humidity=round(st.mean(hum),2)
# print(temperature, humidity)
    return temperature, humidity
    # base_url="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/%22+city_name+%22?key=C4KHAUSYXVKSS2565PV7MDC5T"
    # response=requests.get(base_url)
    # x = response.json()
    # y=x['days']
    # temp=[]
    # hum=[]
    # for days in y:
    #   temp.append((days['tempmax']+days['tempmin'])/2)
    #   hum.append(days['humidity'])
    # temperature=st.mean(temp)
    # temperature=round(((temperature-32)*(5/9)),2)
    # humidity=round(st.mean(hum),2)
    # return temperature, humidity

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

#error page

@ app.route('/error')
def error():
    title = 'Crop Connect - Error'
    return render_template('try_again.html', title=title)

# ===============================================================================================

# CROP DATA ROUTING

@ app.route('/apple')
def apple():
    title = 'Crop Connect - Apple'
    return render_template('1-apple.html', title=title)

@ app.route('/banana')
def banana():
    title = 'Crop Connect - Banana'
    return render_template('2-banana.html', title=title)

@ app.route('/blackgram')
def blackgram():
    title = 'Crop Connect - Blackgram'
    return render_template('3-blackgram.html', title=title)

@ app.route('/chickpea')
def chickpea():
    title = 'Crop Connect - Chickpea'
    return render_template('4-chickpea.html', title=title)

@ app.route('/coconut')
def coconut():
    title = 'Crop Connect - Coconut'
    return render_template('5-coconut.html', title=title)

@ app.route('/coffee')
def coffee():
    title = 'Crop Connect - Coffee'
    return render_template('6-coffee.html', title=title)

@ app.route('/cotton')
def cotton():
    title = 'Crop Connect - Cotton'
    return render_template('7-cotton.html', title=title) 

@ app.route('/grapes')
def grapes():
    title = 'Crop Connect - Grapes'
    return render_template('8-grapes.html', title=title) 

@ app.route('/jute')
def jute():
    title = 'Crop Connect - Jute'
    return render_template('9-jute.html', title=title)


@ app.route('/kidneybeans')
def kidneybeans():
    title = 'Crop Connect - Kidneybeans'
    return render_template('10-kidneybeans.html', title=title)

@ app.route('/lentil')
def lentil():
    title = 'Crop Connect - Lentil'
    return render_template('11-lentil.html', title=title)

@ app.route('/maize')
def maize():
    title = 'Crop Connect - Maize'
    return render_template('12-maize.html', title=title)

@ app.route('/mango')
def mango():
    title = 'Crop Connect - Mango'
    return render_template('13-mango.html', title=title)

@ app.route('/mothbeans')
def mothbeans():
    title = 'Crop Connect - Mothbeans'
    return render_template('14-mothbeans.html', title=title)

@ app.route('/mungbean')
def mungbean():
    title = 'Crop Connect - Mungbean'
    return render_template('15-mungbean.html', title=title)

@ app.route('/muskmelon')
def muskmelon():
    title = 'Crop Connect - Muskmelon'
    return render_template('16-muskmelon.html', title=title)

@ app.route('/orange')
def orange():
    title = 'Crop Connect - Orange'
    return render_template('17-orange.html', title=title)

@ app.route('/papaya')
def papaya():
    title = 'Crop Connect - Papaya'
    return render_template('18-papaya.html', title=title)

@ app.route('/pigeonpeas')
def pigeonpeas():
    title = 'Crop Connect - Pigeonpeas'
    return render_template('19-pigeonpeas.html', title=title)

@ app.route('/pomegranate')
def pomegranate():
    title = 'Crop Connect - pomegranate'
    return render_template('20-pomegranate.html', title=title)

@ app.route('/rice')
def rice():
    title = 'Crop Connect - Rice'
    return render_template('21-rice.html', title=title)

@ app.route('/watermelon')
def watermelon():
    title = 'Crop Connect - Watermelon'
    return render_template('22-watermelon.html', title=title)

# Either add more or dynamic

@ app.route('/dynacrop')
def dynacrop():
    title = 'Crop Connect - {{crop}}'
    return render_template('cc-dynacrop.html', title=title)   

# FAQ page

@ app.route('/faq')
def faq():
    title = 'Crop Connect - FAQ'
    return render_template('cc-faq.html', title=title) 


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
            print(temperature,humidity,file=sys.stderr)
            data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
            my_prediction = crop_recommendation_model.predict(data)
            final_prediction = my_prediction[0]

            return render_template('cc-crop-result2.html', prediction=final_prediction, title=title)

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

            return render_template('cc-yield-result2.html', crop_val=crp, my_prediction=round(my_prediction[0],3) , prediction=round(final_prediction,3), title=title)
        else:

            return render_template('try_again.html', title=title) 
# ===============================================================================================
if __name__ == '__main__':
    app.run(debug=False)
