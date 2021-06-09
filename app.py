import streamlit as st
import pandas as pd
import os
import time
import requests


import sys



header = st.beta_container()
dataset = st.beta_container()
features = st.beta_container()

model_training =st.beta_container()

with header :
    st.title("welcome to AQI prediction project")
    st.text(" IN this project I look into trends of AQI in different countries of the world ")

with dataset:
    st.header(" World AQI Dataset ")
    st.text(" I found this dataset at :aqicn.org ")

    city= st.text_input("Enter you city")
    st.write("click on this link to get the api key  for dataset :  https://aqicn.org/data-platform/token/#/")
    
    apikey= st.text_input("Enter the api key or token  you got : ")
    url = 'https://api.waqi.info/feed/'+city+'/?token='
   
    
    
    main_url=  url+apikey
    r=requests.get(main_url)
    data=r.json()
    #data
    d1=data['data']
    aqi=d1['aqi']
    iaqi=d1['iaqi']
    for i in iaqi.items():
        st.write(i[0], ":", i[1]["v"])



with features:
      st.header(" The features created ")
      st.markdown("first feature")
      st.markdown("second feature")
      dew =iaqi.get('dew', 'Nil')
      dew =iaqi.get('dew', 'Nil')
      no2 =iaqi.get('no2', 'Nil')
      o3 =iaqi.get('o3', 'Nil')
      so2 =iaqi.get('so2', 'Nil')
      pm10 =iaqi.get('pm10', 'Nil')
      pm25 =iaqi.get('pm25', 'Nil')

      print(f'(city) AQI :',aqi, '\n')
      print('Individual Air Quality')
      print("Dew :", dew)
      print("no2 :", no2)
      print("o3 :", o3)
      print("so2 :", so2)
      print("pm10 :", pm10)
      print("pm25 :", pm25)


      import matplotlib.pyplot as plt
      import matplotlib.pyplot as plt
      pollutants =[i for i in iaqi]
      values = [i ['v'] for i in iaqi.values()]

      print(pollutants)
      print(values)

      explode= [0 for i in pollutants]
      mx = values.index(max(values))
      explode[mx] = 0.1
      plt.figure(figsize=(8,6))

      plt.pie(values, labels= pollutants, autopct="%1.1f%%",shadow=True)
      plt.show()



with  model_training:
     st.header("Time to train the model ")
     st.text("Here you get to choose the hyperparameters of the model And see the evolution and trends")
     
     

