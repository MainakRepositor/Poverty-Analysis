"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st
import streamlit.components.v1 as components

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Random Forest Classifier</b> for the Poverty Analysis.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    
    Population = st.slider("Population", float(df["Population"].min()), float(df["Population"].max()))
    Literacy_Index = st.slider("Literacy Rate", float(df["Literacy_Index"].min()), float(df["Literacy_Index"].max()))
    Poverty_Index = st.slider("Poverty Index", float(df["Poverty_Index"].min()), float(df["Poverty_Index"].max()))
    Standard_of_Life = st.slider("Standard of Living", float(df["Standard_of_Life"].min()), float(df["Standard_of_Life"].max()))
    Hunger_Index = st.slider("Hunger Index", float(df["Hunger_Index"].min()), float(df["Hunger_Index"].max()))
    Satisfaction_Level = st.slider("Governance Satisfaction", float(df["Satisfaction_Level"].min()), float(df["Satisfaction_Level"].max()))
    Healthcare = st.slider("Healthcare Satisfaction", float(df["Healthcare"].min()), float(df["Healthcare"].max()))
    Basic_Needs = st.slider("Basic Needs", float(df["Basic_Needs"].min()), float(df["Basic_Needs"].max()))
     
    

    # Create a list to store all the features
    features = [Population,Literacy_Index,Poverty_Index,Standard_of_Life,Hunger_Index,Satisfaction_Level,Healthcare,Basic_Needs]

    # Create a button to predict
    if st.button("Detect Class"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score
        

        # Prfloat the output according to the prediction
                
        if (prediction == 2):
            st.error("Extremely poor! On brink of poverty")
            
        elif (prediction == 3):
            st.error("Very Poor! Need financial aids")
          
        elif (prediction == 4):
            st.error("Poor! Need financial aids")
     
        elif (prediction == 5):
            st.warning("Average. Need good governance")
      
        elif (prediction == 6):
            st.warning("Good! Well to do")
    
        elif (prediction == 7):
            st.warning("Very good! Significantly good.")

        elif (prediction == 8):
            st.success("Prosperous State! Doing good.")
    
        elif (prediction == 9):
            st.success("Magnificient! Surplus aids present")
  
        elif (prediction == 10):
            st.success("Extremely Good and Rich State")
 
        
        # Prfloat teh score of the model 
        st.sidebar.write("The model used is trusted by beaurocratists and has an accuracy of ", round((score*100),2),"%")
