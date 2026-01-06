########################################## Importing the necessary Packages##########################################################################
import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import numpy as np
from PIL import Image
import plotly.express as px

df3 = pd.read_excel('Data_Table.xlsx', sheet_name= 'Third')

def app():
    st.subheader("Target Features")
    st.write("This is about understanding the target features and their distributions")
    options = st.sidebar.selectbox("Select One", ("Classification_Target", "Regression_Target"))
    if options == "Classification_Target":
        st.subheader("Classification_Target")
        st.write("✨ **Porosity Label** Distribution Plot")
        fig = px.histogram(x=df3['Porosity Label'], title='Count Plot', labels={'x': 'Porosity Label', 'y': 'Frequency'})
        st.plotly_chart(fig)
        with st.beta_expander("Inferences"):
                    st.write("1. This is a highly **Imbalanced Data**, where there are **1490 Instances** of **No Porosity** and **70 Instances** of **Porosity**")
                    st.write("2. The **Porosity Label** is **classification label** and  **Porosity Size (mm)** is the **regression label**")
    if options == "Regression_Target":
        st.subheader("Regression_Target")
        st.write("✨ **Porosity Size** Distribution Plot")
        fig = px.histogram(x=df3['Porosity Size (mm)'], title='Count Plot', labels={'x': 'Porosity Size (mm)', 'y': 'Frequency'})
        st.plotly_chart(fig)
        with st.beta_expander("Inferences"):
                    st.write("1. Surprisingly, the **regression target** has **1490 instances** of **Zeros** anf **70 instances** of **non-zero**")
                    st.write("2. This makes it a **Zero Inflated Data**")
