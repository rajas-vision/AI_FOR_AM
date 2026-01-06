import streamlit as st
import pandas as pd
import pickle
import numpy as np
import random
import os, csv, cv2, glob, imageio, pylab
from PIL import Image

from tensorflow.keras.models import Model
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input

with open('random_forest_classifier.pkl', 'rb') as file:
    loaded_rf_classifier = pickle.load(file)
    
with open('random_forest_regressor.pkl', 'rb') as file:
    loaded_rf_regressor = pickle.load(file)

#Importing models
classifier = pickle.load(open("random_forest_classifier.pkl", "rb"))
regressor = pickle.load(open("random_forest_regressor.pkl", "rb"))

model = VGG16()
model = Model(inputs = model.inputs, outputs = model.layers[-2].output)


def extract_features(img, model):
    reshaped_img = np.reshape(cv2.resize(img, (224,224)), (1, 224, 224, 3))
    imgx = preprocess_input(reshaped_img)
    features = model.predict(imgx, use_multiprocessing=True)
    return features
      

#########################################################################################################################################################################
def app():   
    Select_An_Image = ['Image_1', 'Image_2', 'Image_3']
    options = st.sidebar.selectbox('Which Image would you like to Select?', Select_An_Image)
    ###############################################################################################################
    if options == "Image_1":
        st.subheader("The Selected Image is `Image_1`")
        st.write("`Ground Truth`: **Porosity Label : 1**")
        image1 = Image.open('image 1.png')
        st.image(image1, use_column_width=True)
        img1 = cv2.imread('image 1.png')
        data1 = list(extract_features(img1, model)[0])
        a = np.array(data1)
        a = a.reshape(1, -1)
        clas_pred = classifier.predict(a)
        reg_pred = regressor.predict(a)
        if st.button("Predict"):
            st.write("The prediction is `{}` which is`Porosity Present`".format(clas_pred))
            st.write("The Porosity Size is `{} mm`".format(reg_pred))
            
    if options == "Image_2":
        st.subheader("The Selected Image is `Image_2`")
        st.write("`Ground Truth`: **Porosity Label : 1**")
        image2 = Image.open('image 2.png')
        st.image(image2, use_column_width=True)
        img2 = cv2.imread('image 2.png')
        data2 = list(extract_features(img2, model)[0])
        a = np.array(data2)
        a = a.reshape(1, -1)
        clas_pred = classifier.predict(a)
        reg_pred = regressor.predict(a)
        if st.button("Predict"):
            st.write("The prediction is `{}` which is`Porosity Present`".format(clas_pred))
            st.write("The Porosity Size is `{} mm`".format(reg_pred))
    if options == "Image_3":
        st.subheader("The Selected Image is `Image_3`")
        st.write("`Ground Truth`: **Porosity Label : 0**")
        image3 = Image.open('image 7.png')
        st.image(image3, use_column_width=True)
        img3 = cv2.imread('image 7.png')
        data3 = list(extract_features(img3, model)[0])
        a = np.array(data3)
        a = a.reshape(1, -1)
        clas_pred = classifier.predict(a)
        reg_pred = regressor.predict(a)
        if st.button("Predict"):
            st.write("The prediction is `{}` which is`Porosity Not Present`".format(clas_pred))
            #st.write("The Porosity Size is `{} mm`".format(reg_pred))   