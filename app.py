import streamlit as st
from PIL import Image
import cv2
import os
import sys
import time
from modules.navbar import *
from modules.opencv import *
from modules.style import *
import numpy as np
import pandas as pd

code = '''
def hello():
    print("Hello, Streamlit!")
'''
NAV_OPTIONS = ('Image Information', 'Grayscale', 'Color Extraction', 'Shifting', 'Rotation', 'Resize', 'Blurring', 'Histogram')

if __name__ == '__main__':
    st.beta_set_page_config(page_title='CV-Learn', page_icon='None', layout='centered', initial_sidebar_state='expanded')
    st.set_option('deprecation.showfileUploaderEncoding', False)
    st.title('**Welcome to CV-Learn** :sunglasses:')  
    st.sidebar.title('Navigation')
    
    local_css("style.css")
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
    # icon("search")

    # progress_bar = st.progress(0)
    # status_text = st.empty()
    # for i in range(100):
    #     progress_bar.progress(i + 1)
    #     status_text.text(str(i)+'%')
    #     time.sleep(0.05)
    # status_text.text('Done!')

    # """Add this in your streamlit app.py"""
    # GA_JS = """Hello world!"""

    # # Insert the script in the head tag of the static template inside your virtual environement
    # index_path = pathlib.Path(st.__file__).parent / "static" / "index.html"
    # soup = BeautifulSoup(index_path.read_text(), features="lxml")
    # if not soup.find(id='custom-js'):
    #     script_tag = soup.new_tag("script", id='custom-js')
    #     script_tag.string = GA_JS
    #     soup.head.append(script_tag)
    #     index_path.write_text(str(soup))

    selection = st.sidebar.selectbox('What would you like to do?', NAV_OPTIONS)
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
        mod_image = navbar(upload_image_array, channels, selection)
        if mod_image is not None:
            if channels == 3 and selection != 'Grayscale':
                st.image(mod_image, caption='Modified Image', width=None, channels='BGR')
            elif channels != 3 or selection == 'Grayscale':
                st.image(mod_image, caption='Modified Image', width=None)

    st.sidebar.subheader('Contribution')
    st.sidebar.info('This is an open source project and you are welcome to contribute your awesome comments, questions and resources as issues or pull requests to the source code.')
    st.sidebar.subheader('About')
    st.sidebar.info('This app is maintained by Prateek Goyal. You can learn more about me at: https://prateekgoyal18.github.io/')

    # st.sidebar.subheader('Contribution')
    # st.sidebar.markdown('''<div class="card">
    #     <span>This is an open source project and you are welcome to contribute your awesome comments, questions and resources as issues or pull requests to the source code.</span>
    #     </div>''', unsafe_allow_html=True)
    # st.sidebar.subheader('About')
    # st.sidebar.markdown('''<div class="card">
    #     <span>This app is maintained by Prateek Goyal. You can learn more about me <a class="link" href="https://prateekgoyal18.github.io/" target="_blank">here</a>.</span>
    #     </div>''', unsafe_allow_html=True)