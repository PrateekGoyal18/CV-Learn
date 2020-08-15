import streamlit as st
from PIL import Image
import os
import sys
from modules.sidebar import sidebar
import numpy as np

code = '''
def hello():
    print("Hello, Streamlit!")
'''

if __name__ == '__main__':
    st.set_option('deprecation.showfileUploaderEncoding', False)

    st.title('**Welcome to CV-Learn** :sunglasses:')
    
    st.sidebar.title('Options')

    image_file = st.file_uploader("Choose an image", type=["png", "jpg", "jpeg"])
    if image_file is not None:
        image = Image.open(image_file)
        st.image(image, caption='Uploaded Image', use_column_width=True)
        img_array = np.array(image)
        # st.code(code, language='python')

        selection = st.sidebar.selectbox('What would you like to do?',
        ('Color Extraction', 'Shifting', 'Rotation', 'Resize'))
        mod_image = sidebar(img_array, selection)
        st.image(mod_image, caption='Modified Image', use_column_width=True)