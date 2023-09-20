from PIL import Image
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Stephan Griesel", page_icon=":waving_hand:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

#Assets
lottie_coding = load_lottieurl("https://assets-v2.lottiefiles.com/a/2d4bf306-116e-11ee-94dd-43b1d64018e2/FyKvMAcxtP.json")
img_screen = Image.open("images/screen.png")

#Header
with st.container():
    st.subheader("Hi, I am Stephan :wave:")
    st.title("Web Developer from Netherlands")
    st.write("Always Curious")
    st.write("[GitHub >](http://www.github.com/stephangriesel)")

#What I do
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Curabitur tempor molestie nunc a dapibus. Aliquam fringilla dui a tortor feugiat commodo. Maecenas pellentesque, est commodo luctus placerat, ex erat cursus mauris, nec viverra nibh ligula vulputate nisi. Aliquam erat volutpat. Aliquam erat volutpat. Sed accumsan, metus eget venenatis bibendum, sapien dui aliquam nulla, at feugiat erat mi rutrum quam. Aenean ac volutpat lorem. Praesent pellentesque dignissim tristique. Proin et convallis dolor, quis scelerisque mi. Aenean cursus, libero sit amet convallis fermentum, ante mi semper quam, at vulputate ex ante quis ipsum. Mauris velit metus, elementum vitae nulla ultricies, tempor suscipit lorem. Suspendisse in viverra neque. Morbi ornare lectus in ipsum rhoncus, ut rutrum neque sodales. Pellentesque id aliquam arcu.
            """
            )
        st.write("[Github >](https://www.github.com/stephangriesel)")
    with right_column:
        st_lottie(lottie_coding, height=500, key="coding")

#Portfolio
with st.container():
    st.write("---")
    st.header("My Portfolio")
    st.write("##")
    image_column, text_column = st.columns((1,2))
    with image_column:
        st.image(img_screen)
    with text_column:
        st.subheader("Some of my projects")
        st.write(
            """
            Blah blah blah
            """
        )
        st.markdown("[Github](https://www.github.com/stephangriesel)")

#Contact
with st.container():
    st.write("---")
    st.header("Get in touch!")
    st.write("##")
    
    contact_form = """
    <form action="https://formsubmit.co/sgriesel@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
        <button type="submit">Send</button>
     </form>
     """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()