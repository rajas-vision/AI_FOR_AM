
import streamlit as st
from PIL import Image


def app():
    st.header("✨ **About The Team**")
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        image1 = Image.open('Keval.jpg')
        st.header("`Keval Parmar`")
        st.image(image1, use_column_width=True)
        with st.beta_expander("About"):
            st.write("`Robotics GRAD Student` at ASU, with a passion for Mechatronics & AI")
                                              
    with col2:
        image2 = Image.open('pius.jpg')
        st.header("`Pius Gyamenah`")
        st.image(image2, use_column_width=True)
        with st.beta_expander("About"):
            st.write("`PhD Student` in `manufacturing engineering` `School of manufacturing systems and networks`")
            
    with col3:
        image3 = Image.open('karteek.jpg')
        st.header("`Karteek Menda`")
        st.image(image3, use_column_width=True)
        with st.beta_expander("About"):
            st.write("`Robotics GRAD Student` at ASU, `Ex - Data Science Professional`, and a `Machine Learning Blogger`")
            st.write("`Experienced data science professional` with `extensive knowledge` of building `data-intensive applications` and overcoming `complex architectural` and scalability challenges")


    st.header("**Some Background**")
    st.markdown("✨ **Unlike subtractive manufacturing techniques, additive manufacturing, sometimes referred to as 3D printing, is a family of technologies that deposit and consolidate materials to build a three-dimensional item**")
    st.markdown("✨ **One of the most widely used additive manufacturing methods is fused deposition modelling (FDM), and many more which has shown to have several uses in a variety of sectors, including automotive, aerospace, and medical prosthetics**")
    st.markdown("✨ **Because most of all AM process is a thermal process, it has the potential to reduce the mechanical qualities of the thermoplastics by introducing internal spaces and pores**")
    st.markdown("✨ **Through machine learning  modelling and testing from frame-wise thermal images, this model seeks to understand how the minute holes affect the mechanical characteristics of material created using these AM technique**")

    st.header("✨ **About the Process**")
    st.markdown("✨ **X-ray computed tomography (XCT) was used to quantitatively characterise the three-dimensional microscopic details of the internal pores, such as size, shape, density, and spatial location**")
    st.markdown("✨ **This was followed by experiments to characterise the mechanical properties of the material**")
    st.markdown("✨ **A micromechanical model was developed to forecast the mechanical characteristics of the material as a function of porosity, which is the ratio of the total volume of the pores to the total volume of the material, based on the microscopic features of the pores as identified by XCT**")
    st.markdown("✨ **Using a liquefier head, a computer-controlled nozzle is used to melt thermoplastic filament, which is then extruded and placed onto a platform to manufacture the part layer by layer in the AM processes**")
    st.markdown("✨ **The actual manufacturing process involves heat, which introduces heterogeneities in the micro/meso length scale, particularly voids and pores, the size, shape, and spatial distribution of which are greatly influenced by the process parameters**")
    st.markdown("✨ **These holes and voids might have an impact on the deposited materials' internal structure, which could then have an impact on the finished product's mechanical qualities**")

    st.header("**About the Modelling**")
    st.markdown("✨ **We selected the pore labels and size as our classification and regressing features respectively, as the pores are universally going to be present in every AM manufactured commodity, their shape, size, temperature are going to change as the materials changes**")
    st.markdown("✨ **If we can determine pore size from frame wise images we can easily and accurately anticipate the mechanical properties with calculations**")
    st.markdown("✨ **Therefore, the internal pores are an important quality and less researched feature, so we designed ML model predicting the pore size**")
    
    
   




