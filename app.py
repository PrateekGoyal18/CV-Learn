import streamlit as st
from PIL import Image
import os
import sys
from modules.navbar import *
from modules.opencv import *
import numpy as np

code = '''
def hello():
    print("Hello, Streamlit!")
'''
NAV_OPTIONS = ('Image Information', 'Grayscale', 'Color Extraction', 'Shifting', 'Rotation', 'Resize')

if __name__ == '__main__':
    st.beta_set_page_config(page_title='CV-Learn', page_icon=None, layout='centered', initial_sidebar_state='expanded')
    st.set_option('deprecation.showfileUploaderEncoding', False)
    st.title('**Welcome to CV-Learn** :sunglasses:')  
    st.sidebar.title('Navigation')
    st.markdown('''<style type="text/css"> 
        .card { background-color: #dde9f3; border: 1px solid #dde9f3; border-radius: 5px; padding: 5px; color: #296e7f; } 
        .link, .link:hover { text-decoration: underline; color: #1e6777 !important; font-weight: bold; }
        .image-info { display: flex; flex-wrap: wrap; text-align: center; justify-content: center; }
        .section { margin: 8px; padding: 20px; background-color: #cfe8cf; border: 1px solid #cfe8cf; border-radius: 15px; color: #3e613e; width: 215px; text-align: center; }
        .section:hover { box-shadow: 6px 7px 19px -1px #537853; }
        </style>''', unsafe_allow_html=True)

    selection = st.sidebar.selectbox('What would you like to do?', NAV_OPTIONS)

    image_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption='Uploaded Image', width=None, channels='BGR')
        img_array = np.array(image)
        channels = img_array.ndim
        # st.code(code, language='python')

        mod_image = navbar(img_array, channels, selection)
        if mod_image is not None:
            if channels == 3:
                st.image(mod_image, caption='Modified Image', width=None, channels='RGB')
            else:
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