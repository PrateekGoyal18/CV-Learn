import streamlit as st
from PIL import Image
import cv2
import os
import sys
import time
from modules.image_options import *
from modules.opencv import *
from modules.style import *
from modules.pages import *
import numpy as np
import pandas as pd

PAGE_NAV_OPTIONS = ('Home', 'Image Options', 'About')
IMAGE_NAV_OPTIONS = ('Image Information', 'Grayscale', 'Color Extraction', 'Shifting', 'Rotation', 'Resize', 'Blurring', 'Histogram')

def page(page_name):
    if page_name == PAGE_NAV_OPTIONS[0]:
        progress_bar = st.progress(0)
        status_text = st.empty()
        for i in range(100):
            progress_bar.progress(i + 1)
            status_text.text(str(i)+'%')
            time.sleep(0.03)
        status_text.text('Done!')
        st.subheader('Holla!')
        st.write('Welcome to the world of Computer Vision. Here you will not just be learning Image Processing, but you will also get to experience it with real-world example pictures.')
        st.write("Let's dive in to know more.")
        if st.button('Proceed'):
            pass
            # page_name = PAGE_NAV_OPTIONS[1]
            # page(page_name)
    
    elif page_name == PAGE_NAV_OPTIONS[1]:
        image_func = st.sidebar.selectbox('What would you like to do?', IMAGE_NAV_OPTIONS)
        image_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
        if image_file is not None:
            image = Image.open(image_file)
            img_array = np.array(image)
            channels = img_array.ndim
            if channels == 3:
                upload_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                st.image(upload_image, caption='Uploaded Image', width=None, channels='BGR')
            else:
                upload_image = image
                st.image(upload_image, caption='Uploaded Image', width=None)
            # st.code(code, language='python')

            upload_image_array = np.array(upload_image)
            mod_image = image_op(upload_image_array, channels, image_func)
            if mod_image is not None:
                if channels == 3 and image_func != 'Grayscale':
                    st.image(mod_image, caption='Modified Image', width=None, channels='BGR')
                elif channels != 3 or image_func == 'Grayscale':
                    st.image(mod_image, caption='Modified Image', width=None)

    elif page_name == PAGE_NAV_OPTIONS[2]:
        st.subheader('Contribution')
        st.info('This is an open source project and you are welcome to contribute your awesome comments, questions and resources as issues or pull requests to the source code.')
        st.subheader('About')
        st.info('This app is maintained by Prateek Goyal. You can learn more about me at: https://prateekgoyal18.github.io/')
        st.markdown('''<div class="icons">
            <a href="#"><img src="../assets/img/python.png"></a>
            <a href="#"><img src="../assets/img/streamlit.png"></a>
            <a href="#"><img src="../assets/img/opencv.png"></a>
            <a href="#"><img src="../assets/img/heroku.png"></a>
        </div>''', unsafe_allow_html=True)