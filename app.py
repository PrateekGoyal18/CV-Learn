import streamlit as st
from PIL import Image
import os
import sys
from modules.navbar import navbar
import numpy as np

code = '''
def hello():
    print("Hello, Streamlit!")
'''

if __name__ == '__main__':
    st.set_option('deprecation.showfileUploaderEncoding', False)

    st.title('**Welcome to CV-Learn** :sunglasses:')
    
    st.sidebar.title('Navigation')

    image_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        img_array = np.array(image)
        # st.code(code, language='python')

        selection = st.sidebar.selectbox('What would you like to do?',
        ('Color Extraction', 'Shifting', 'Rotation', 'Resize'))
        mod_image = navbar(img_array, selection)
        st.image(mod_image, caption='Modified Image', use_column_width=True)


    st.sidebar.subheader('Contribution')
    st.sidebar.markdown('''<div style="background-color: #dde9f3; border: 1px solid #dde9f3; border-radius: 5px; padding: 5px; color: #528b9d;">
        This is an open source project and you are welcome to contribute your awesome comments, questions and resources as issues or pull requests to the source code.</div>''', unsafe_allow_html=True)
    st.sidebar.subheader('About')
    st.sidebar.markdown('''<div style="background-color: #dde9f3; border: 1px solid #dde9f3; border-radius: 5px; padding: 5px; color: #528b9d;">
        This app is maintained by Prateek Goyal. You can learn more about me at.''', unsafe_allow_html=True)

    # back: #dde9f3
    # font: #528b9d
    # href: #3c7e9c