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

code = '''
def hello():
    print("Hello, Streamlit!")
'''
PAGE_NAV_OPTIONS = ('Home', 'Image Options', 'About')
IMAGE_NAV_OPTIONS = ('Image Information', 'Grayscale', 'Color Extraction', 'Shifting', 'Rotation', 'Resize', 'Blurring', 'Histogram')

if __name__ == '__main__':
    st.beta_set_page_config(page_title='CV-Learn', page_icon='None', layout='centered', initial_sidebar_state='expanded')
    st.set_option('deprecation.showfileUploaderEncoding', False)
    st.title('**Welcome to CV-Learn** :sunglasses:')  
    st.sidebar.title('Navigation')
    
    local_css("assets/css/style.css")
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')
    # icon("search")

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

    page_name = st.sidebar.radio('Go to', PAGE_NAV_OPTIONS)
    page(page_name)

    # st.sidebar.subheader('Contribution')
    # st.sidebar.info('This is an open source project and you are welcome to contribute your awesome comments, questions and resources as issues or pull requests to the source code.')
    # st.sidebar.subheader('About')
    # st.sidebar.info('This app is maintained by Prateek Goyal. You can learn more about me at: https://prateekgoyal18.github.io/')

    # st.sidebar.subheader('Contribution')
    # st.sidebar.markdown('''<div class="card">
    #     <span>This is an open source project and you are welcome to contribute your awesome comments, questions and resources as issues or pull requests to the source code.</span>
    #     </div>''', unsafe_allow_html=True)
    # st.sidebar.subheader('About')
    # st.sidebar.markdown('''<div class="card">
    #     <span>This app is maintained by Prateek Goyal. You can learn more about me <a class="link" href="https://prateekgoyal18.github.io/" target="_blank">here</a>.</span>
    #     </div>''', unsafe_allow_html=True)