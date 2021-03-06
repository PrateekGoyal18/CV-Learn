import streamlit as st
from PIL import Image
import cv2
import os
import sys
import time
from modules.image_options import *
from modules.image_functions import *
# from modules.video_options import *
# from modules.video_functions import *
from modules.style import *
from modules.vars import *
import numpy as np
import pandas as pd
from pathlib import Path
import base64
# import imutils

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def page(page_name):
    # --------------------------------- Home Page ---------------------------------
    if page_name == PAGE_NAV_OPTIONS[0]:
        progress_bar = st.progress(0)
        status_text = st.empty()
        for i in range(100):
            progress_bar.progress(i + 1)
            status_text.text(str(i)+'%')
            time.sleep(0.02)
        status_text.text('Done!')
        st.subheader('Hola!')
        st.write('Welcome to the world of Computer Vision. Here you will not just be learning Image Processing, but you will also get to experience it with real-world example pictures.')
        st.write("Let's dive in to know more.")
        st.write('**Click on an option in the navigation bar to the left to do something...**')
    
    # --------------------------------- Image Processing Page ---------------------------------
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

            upload_image_array = np.array(upload_image)
            mod_image, ch = image_op(upload_image_array, channels, image_func)
            if mod_image is not None:
                if ch == 3:
                    st.image(mod_image, caption='Modified Image', width=None, channels='BGR')
                else:
                    st.image(mod_image, caption='Modified Image', width=None)

    # --------------------------------- Video Processing Page ---------------------------------
    # elif page_name == PAGE_NAV_OPTIONS[2]:
    #     # camera = cv2.VideoCapture(0)
    #     # if not camera.isOpened():
    #     #     raise IOError("Cannot open webcam")
    #     video_func = st.sidebar.selectbox('What would you like to do?', VIDEO_NAV_OPTIONS)
    #     video_op(video_func)
    
    # --------------------------------- About Page ---------------------------------
    elif page_name == PAGE_NAV_OPTIONS[2]:
        st.subheader('Contribution')
        st.info('This is an open source project and you are welcome to contribute your awesome comments, questions and resources as issues or pull requests to the [source code](https://github.com/PrateekGoyal18/CV-Learn).')
        st.subheader('About')
        st.info('This app is developed and maintained by Prateek Goyal. You can learn more about me [here](https://prateekgoyal18.github.io/).')

        python = "<a href='https://www.python.org/' target='_blank'><img src='data:image/png;base64,{}' class='img-fluid' id='python'></a>".format(img_to_bytes("./assets/img/python.png"))
        streamlit = "<a href='https://www.streamlit.io/' target='_blank'><img src='data:image/png;base64,{}' class='img-fluid' id='streamlit'></a>".format(img_to_bytes("./assets/img/streamlit.png"))
        opencv = "<a href='https://opencv.org/' target='_blank'><img src='data:image/png;base64,{}' class='img-fluid' id='opencv'></a>".format(img_to_bytes("./assets/img/opencv.png"))
        heroku = "<a href='https://www.heroku.com/' target='_blank'><img src='data:image/png;base64,{}' class='img-fluid' id='heroku'></a>".format(img_to_bytes("./assets/img/heroku.png"))
        div_icons = "<div class='icons' style='display: flex;flex-wrap: wrap;text-align: center; justify-content: center;'>" + python + streamlit + opencv + heroku + "</div>"
        st.subheader('Made with :hearts: by')
        st.markdown(div_icons, unsafe_allow_html=True)
        st.write('and me... :grin:')