"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Poverty Analysis")

    # Add image to the home page
    st.image("./images/home.png")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Poverty, a multifaceted issue, denotes the deprivation of basic necessities, spanning income, education, healthcare, and shelter. It manifests in various forms across regions, impacting livelihoods and perpetuating cycles of disadvantage. Analyzing poverty involves assessing income disparities, access to resources, social inequalities, and structural barriers. Factors like unemployment, inadequate infrastructure, and limited education exacerbate its grip. Addressing poverty requires holistic strategies encompassing economic empowerment, social welfare, and educational reforms to break its cycle, fostering inclusive growth and ensuring equitable opportunities for all individuals and communities.
        </p>
    """, unsafe_allow_html=True)