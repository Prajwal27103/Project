#This is the face of our website
import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image

#emoji syntax :emoji_name:
st.set_page_config(page_title="Invesco",page_icon=":dollar:",layout="wide")

#function to load lottie animation
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()

lottie_coding=load_lottieurl("https://lottie.host/305bdae2-baf1-4753-9c15-2077d91b4cd7/FWBj5Ll1YY.json")

#Styling using CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

#Loading images
img1=Image.open("images/img1.png")
#img2=Image.open("images/img2.png")

# Header section
st.title("INVESCO")
st.subheader("Welcome to the era of Investing :rocket:")
st.write("Revolutionize investing with our app! Utilize AI-driven algorithms for accurate stock market predictions. Stay ahead with real-time insights, interactive charts, and personalized alerts. Maximize profits with data-driven decisions. Your ultimate tool for financial success")
st.write("[About](//paste redirect link here//)")


with st.container():#This is a streamlit container. Optional. To organize code
    left_column,right_column=st.columns(2)#divides webpage in two different columns- left column to write text, right column to paste animation
    with left_column:
        st.header(":coin: GET INTO :coin:")
        #
        # code to login/ sign in
        #
    with right_column:
        st_lottie(lottie_coding,height=300,key="stocks")#height and key are optional parameters
        st.image(img1)

#contact us
contact_form="""
<form action="https://formsubmit.co/psvispute27@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <textarea name="message" placeholder="Your email" required></textarea>
     <button type="submit">Send</button>
</form>
"""

with st.container():
    st.markdown(contact_form,unsafe_allow_html=True)