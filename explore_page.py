import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
@st.cache
def load_data():
    df = pd.read_csv("data.csv")
    return df

df = load_data()

def show_explore_page():
    st.title("Explore Fuel Consumption Prediction using Decision Tree Regression Model")

    st.write(
        """
    ### IIT Kharagpur 2023
    """
    )
    st.write(
        """
    ### Tractor PTO power vs. Fuel Consumption Plot
    """
    )

    res1 = st.write(sns.scatterplot(x="Tractor_PTO", y="FC", data=df))
    st.pyplot(res1)
    st.write(
        """
    ### Engine Speed vs. Fuel Consumption Plot
    """
    )
    res2 = st.write(sns.scatterplot(x="Engine_Speed", y="FC", data=df))
    st.pyplot(res2)
    st.write(
        """
    ### Speed Depression vs. Fuel Consumption Plot
    """
    )
    res3 = st.write(sns.scatterplot(x="Speed_Depression", y="FC", data=df))
    st.pyplot(res3)
    st.write(
        """
    ### Tractor PTO Power Boxplot
    """
    )
    res4 = st.write(sns.boxplot(df['Tractor_PTO']))
    st.pyplot(res4)
    st.write(
        """
    ### Engine Speed (RPM) Boxplot
    """
    )
    res5 = st.write(sns.boxplot(df['Engine_Speed']))
    st.pyplot(res5)
    st.write(
        """
    ### R(Speed Depression)
    """
    )
    res6 = st.write(sns.boxplot(df['Speed_Depression']))
    st.pyplot(res6)
    st.write(
        """
    ### Fuel Consumption (lit/h)
    """
    )
    res7 = st.write(sns.boxplot(df['FC']))
    st.pyplot(res7)
