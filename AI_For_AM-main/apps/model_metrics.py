########################################## Importing the necessary Packages##########################################################################
import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import numpy as np
from PIL import Image


def app():
    st.subheader("Model Metrics")
    st.write("This is basically to display the model metrics")
    options = st.sidebar.selectbox("Select One", ("Classification Model Metrics", "Regression Model Metrics"))
    if options == "Classification Model Metrics":
        st.subheader("Classification Model Metrics")
        st.write("`Model Predicting` **Porosity(1)** or **No Porosity(0)**")
        col1, col2 = st.beta_columns(2)
        with col1:
            image1 = Image.open('Class_Before_Hyper.png')
            st.header("**Classification Metrics** of `Baseline Random Forest Model` with default parameters")
            st.image(image1, use_column_width=True)
            with st.beta_expander("Inferences"):
                    st.write("1. This is a `baseline model` with **default parameters** ane we can see `metrics` like `F1 score` and `ROC_Curve`, which are not performing well on `Minority Class`")
                    st.write("2. `Accuracy` is a `metric trap` over here and the **model is very good at classifying Majority class** and it has **poor performance for minority class** predictions")
                                              
        with col2:
            image2 = Image.open('Class_After_Hyper.png')
            st.header("**Classification Metrics** with `Best Hyperparameters` after `tuning`")
            st.image(image2, use_column_width=True)
            with st.beta_expander("Inferences"):
                    st.write("1. Once hyper parameter tuned we get the best estimators of the model which helps in classifying both majority and minority class")
                    st.write("2. The `Metrics` like `F1 Score`, and `ROC-AUC` have a **fine balance** between **classifying the majority vs minority classes.**")
                    
        col1, col2 = st.beta_columns(2)
        with col1:
            image1 = Image.open('class_before_hyper1.png')
            st.header("**Classification Metrics** of `Baseline XGBoost Model` with default parameters")
            st.image(image1, use_column_width=True)
            with st.beta_expander("Inferences"):
                    st.write("1. This is a `baseline model` with **default parameters** ane we can see `metrics` like `F1 score` and `ROC_Curve`, have improved when compared with the `Random Forest Model`")
                    st.write("2. `Accuracy` is a `metric trap` over here and the **model is very good at classifying Majority class** and it has **considerable* predictive power for minority class**")
                                              
        with col2:
            image2 = Image.open('class_after_hyper1.png')
            st.header("**Classification Metrics** with `Best Hyperparameters` after `tuning`")
            st.image(image2, use_column_width=True)
            with st.beta_expander("Inferences"):
                    st.write("1. Once hyper parameter tuned we get the best estimators of the model which helps in classifying both majority and minority class")
                    st.write("2. The `Metrics` like `F1 Score`, and `ROC-AUC` have a **fine balance** between **classifying the majority vs minority classes, and this model si the best**")
               
                    
    if options == "Regression Model Metrics":
        st.subheader("Regression Model Metrics")
        st.write("`Model Predicting` **Porosity size(mm)**")
        col1, col2 = st.beta_columns(2)
        with col1:
            image3 = Image.open('Reg_Before_Hyper.png')
            st.header("**Regression Metrics** of `Baseline Random Forest Model` with default parameters")
            st.image(image3, use_column_width=True)
            with st.beta_expander("Inferences"):
                    st.write("1. This `zero inflated data` is one **main aspect** why the model is having a **poor performance**, but on this data, the **metrics seems to be convincing**")
                    
                                              
        with col2:
            image4 = Image.open('Reg_After_Hyper.png')
            st.header("**Regression Metrics** with `Best Hyperparameters` after `tuning`")
            st.image(image4, use_column_width=True)
            with st.beta_expander("Inferences"):
                    st.write("1. Even after **Hyper parameter tuning**, we could be able to get a **slight increase** in the main `metrics`")
                  
        col1, col2 = st.beta_columns(2)
        with col1:
            image3 = Image.open('reg_before_hyper1.png')
            st.header("**Regression Metrics** of `Baseline XGboost Model` with default parameters")
            st.image(image3, use_column_width=True)
            with st.beta_expander("Inferences"):
                    st.write("1. This `zero inflated data` is one **main aspect** why the model is having a **poor performance**, but on this data, the **metrics seems to be convincing**")
                    
                                              
        with col2:
            image4 = Image.open('reg_after_hyper1.png')
            st.header("**Regression Metrics** with `Best Hyperparameters` after `tuning`")
            st.image(image4, use_column_width=True)
            with st.beta_expander("Inferences"):
                    st.write("1. Even after **Hyper parameter tuning**, we couldn't be able to get a **slight increase** in the main `metrics`")