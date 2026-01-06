########################################## Importing the necessary Packages##########################################################################
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
############################## Dispaly the features###########################################################################################


#######################################################################################################################################################
def app():
    st.subheader("Data")
    st.write("This is about understanding the parameters, features, summary statistics, and glimpse of the data")
    options = st.sidebar.selectbox("Select One", ("Parameters", "Features", "Summary Statistics", "Glimpse of the Data"))
    if options == "Parameters":
        st.subheader("Parameters")
        st.write("✨ Parametrs with their Summary Values")
        image1 = Image.open('Data_Image.png')
        st.image(image1, use_column_width=True)
        with st.beta_expander("Inferences"):
                    st.write("1. Details about the Pyrometer CSV's")
                    st.write("2. Details of XCT Porosity Labels")
                    st.write("3. Thin Waal Build Parameters")
    
    if options == "Features":
        st.subheader("Features")
        st.write("✨ Features with their description")
        #Import the dataframe
        df1 = pd.read_excel('Data_Table.xlsx', sheet_name= 'First')
        # Display the dataframe in Streamlit
        st.dataframe(df1)
        with st.beta_expander("Inferences"):
                    st.write("1. Here we can see description of each of the features")
                    st.write("2. The **Porosity Label** is **classification label** and  **Porosity Size (mm)** is the **regression label**")
    if options == "Summary Statistics":
        st.subheader("Summary Statistics")
        st.write("✨ Min Max, range of the Numerical features")
        #Import the dataframe
        df2 = pd.read_excel('Data_Table.xlsx', sheet_name= 'Second')
        # Display the dataframe in Streamlit
        st.dataframe(df2)
        with st.beta_expander("Inferences"):
                    st.write("1. Here we can see minimum, maximum and range of each of the numerical features")
                    
    if options == "Glimpse of the Data":
        st.subheader("Glimpse of the Data")
        #Import the dataframe
        df3 = pd.read_excel('Data_Table.xlsx', sheet_name= 'Third')
        # Display the dataframe in Streamlit
        st.dataframe(df3)
        











