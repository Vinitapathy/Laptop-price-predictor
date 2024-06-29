# -*- coding: utf-8 -*-
"""
Created on Sat Jun 24 00:10:39 2023

@author: Hp
"""

import streamlit as st
import pickle as pkl
import pandas as pd
import numpy as np

def MyBG_colour(wch_colour): 
    my_colour = f"<style> .stApp {{background-color: {wch_colour};}} </style>"
    st.markdown(my_colour, unsafe_allow_html=True)

MyBG_colour("yellow")  

# importing the model

model = pd.read_pickle("Model.pkl")
laptops = pd.read_pickle("laptops.pkl")

st.title('Laptop price predictor')

# selecting brand
company = st.selectbox("Select the brand",laptops['Company'].unique())

# selecting type
type = st.selectbox("Select the type",laptops['TypeName'].unique())

# selct the CPU
cpu = st.selectbox("Select the CPU",laptops['Cpu'].unique())

# selecting RAM
ram = st.selectbox("Select the RAM(in GB)",[2,4,6,8,12,16,24,32,64])

# selecting GPU
gpu = st.selectbox("Select the GPU",laptops['Gpu'].unique())

# typing weight
weight = st.number_input('Enter weight')

# touch
touchscreen = st.selectbox("Touchscreen",['Yes','No'])

# IPS
ips = st.selectbox("IPS",['Yes','No'])

# Selecting screen resolution
resolution = st.selectbox("Screen resolution",laptops['Screen_Resolution'].unique())

# OS
os = st.selectbox("Select the OS",laptops['OS'].unique())

if st.button('Predict price'):
	if touchscreen == 'Yes':
		touchscreen = 1
	else:
		touchscreen = 0

	if ips == 'Yes':
		ips = 1
	else:
		ips = 0

	data = [[company,type,cpu,ram,gpu,weight,touchscreen,ips,resolution,os]]

	query = pd.DataFrame(data, columns= ['Company', 'TypeName', 'Cpu', 'Ram', 'Gpu', 'Weight','touchscreen','IPS','Screen_Resolution','OS'])
       
	 
	st.title("The predicted price for this laptop is {}" .format(np.exp(model.predict(query))))
    
                     
                     