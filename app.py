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
    aqi= data['aqi']
    iaqi = data['iaqi']
    for i in iaqi.items():
        print(i[0],":",i[1]['v'])



with features:
      st.header(" The features created ")
      st.markdown("first feature")
      st.markdown("second feature")





with  model_training:
     st.header("Time to train the model ")
     st.text("Here you get to choose the hyperparameters of the model And see the evolution and trends")
     
     

