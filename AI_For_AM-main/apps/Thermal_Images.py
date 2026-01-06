########################################## Importing the necessary Packages##########################################################################
import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import numpy as np
from PIL import Image


def app():
    st.subheader("Thermal Images")
    st.write("This is basically to display the **Porous and non porous Thermal Images**")
    options = st.sidebar.selectbox("Select One", ("Porous Thermal Images", "Non-Porous Thermal Images"))
    if options == "Porous Thermal Images":
        st.subheader("Porous Thermal Images")
        st.write("This is about understanding the Porous Thermal Images")
        col1, col2, col3 = st.beta_columns(3)
        with col1:
            image1 = Image.open('image 1.png')
            st.header("Porosity `Image 1`")
            st.image(image1, use_column_width=True)
                                              
        with col2:
            image2 = Image.open('image 2.png')
            st.header("Porosity `Image 2`")
            st.image(image2, use_column_width=True)
            
        with col3:
            image3 = Image.open('image 3.png')
            st.header("Porosity `Image 3`")
            st.image(image3, use_column_width=True)        
                    
    if options == "Non-Porous Thermal Images":
        st.subheader("Non-Porous Thermal Images")
        st.write("This is about understanding the Non-Porous Thermal Images")
        
        col1, col2 = st.beta_columns(2)
        with col1:
            image7 = Image.open('image 7.png')
            st.header("Non Porosity `Image 7`")
            st.image(image7, use_column_width=True)
                                              
        with col2:
            image27 = Image.open('image 27.png')
            st.header("Non Porosity `Image 27`")
            st.image(image27, use_column_width=True)