from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Something about me", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#use local css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#-------LOAD ASSETS----
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_0yfsb3a1.json")
img_pp = Image.open("creating website/pp.jpeg")
img_python = Image.open("creating website/python.jpeg")

#-----HEADER SECTION-----
with st.container():
    st.subheader("Hi,I am Yash ⚡")
st.title("A genius boy from Jabalpur")
st.write("I am passionate about making programming easier for people to learn it and even I am not able to learn languages like Java and I only know python")
st.write("[for more information visit this channel >](https://youtube.com/@CodeWithHarry)")

# --------WHAT I DO ------
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("WHY DO I WANT TO MAKE CODING EASIER-")
        st.write("##")
        st.write("I want to make it easier to learn coding because it becomes very difficult for many people to learn programming languages like Java.I want to make programming interesting not boring.")
        st.write("[This is another youtube channel that can help you >](https://youtube.com/@ApnaCollegeOfficial)")
with right_column:
    st_lottie(lottie_coding, height=300, key="coding")
    st.image(img_python)
    st.image(img_pp)

with left_column:
    st.subheader("I think python is a very good programming language for developing websites")
    st.write("Just learn python and go ahead")
    st.markdown("[Watch Video >](https://youtube.com/@CodeWithHarry)")

    #----CONTACT---
    with st.container():
        st.write("---")
        st.header("Get in touch with me!")
        st.write("##")

        #Documentation
        contact_form = """
        <form action="https://formsubmit.co/shailendrawadhwani84@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message" required></textarea>
        <button type="submit">Send</button>
</form>
"""
left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()