import streamlit as st
from modules.opencv import *

IMAGE_NAV_OPTIONS = ('Image Information', 'Grayscale', 'Color Extraction', 'Shifting', 'Rotation', 'Resize', 'Blurring', 'Histogram')

def image_op(image, channels, selection):
    if selection == IMAGE_NAV_OPTIONS[0]:
        if channels == 3:
            channels = str(3) + ' (RGB)'
        else:
            channels = str(1) + ' (Grayscale)'
        st.markdown('''<div class="image-info">
            <div class="section">Height/Rows: ''' + str(image.shape[0]) + '''</div>
            <div class="section">Width/Columns: ''' + str(image.shape[1]) + '''</div>
            <div class="section">Channels: ''' + channels + '''</div>
            </div>''', unsafe_allow_html=True)
        mod_image = None

    elif selection == IMAGE_NAV_OPTIONS[1]:
        if channels == 3:
            mod_image = grayscale(image)
        else:
            st.warning('The image is already in Grayscale Mode!!')
            mod_image = None

    elif selection == IMAGE_NAV_OPTIONS[2]:
        if channels == 3:
            color = st.sidebar.radio("Select the color you want to extract", ('Red', 'Blue', 'Green'))
            mod_image = extract(image, color)
        else:
            st.warning('The image is not in RGB format!!')
            mod_image = None

    elif selection == IMAGE_NAV_OPTIONS[3]:
        x = st.sidebar.slider('Select the x-axis value', 0, image.shape[1])
        y = st.sidebar.slider('Select the y-axis value', 0, image.shape[0])
        mod_image = shift(image, x, y)

    elif selection == IMAGE_NAV_OPTIONS[4]:
        rotate_type = st.sidebar.radio("Select the sub-feature", ('Basic Rotation', 'Bound Rotation'))
        if rotate_type == 'Basic Rotation':
            angle = st.sidebar.slider('Select an angle', -360.0, 360.0)
            mod_image = rotate(image, angle, bound=False)
        else:
            angle = st.sidebar.slider('Select an angle', -360.0, 360.0)
            mod_image = rotate(image, angle, bound=True)

    elif selection == IMAGE_NAV_OPTIONS[5]:
        resize_type = st.sidebar.radio("Select the sub-feature", ('Without Aspect Ratio', 'With Aspect Ratio'))
        if resize_type == 'Without Aspect Ratio':
            width = st.sidebar.number_input('Enter the width:', min_value=1)
            height = st.sidebar.number_input('Enter the height:', min_value=1)
            if width == 1:
                (dim, mod_image) = resize(image, height=int(height), AR=False)
            elif height == 1:
                (dim, mod_image) = resize(image, width=int(width), AR=False)
            else:
                (dim, mod_image) = resize(image, width=int(width), height=int(height), AR=False)
        else:
            width = st.sidebar.number_input('Enter the width:', min_value=2)
            height = st.sidebar.number_input('Enter the height:', min_value=2)
            if width == 2 and height != 2:
                (dim, mod_image) = resize(image, width=None, height=int(height), AR=True)
            elif width != 2 and height == 2:
                (dim, mod_image) = resize(image, width=int(width), height=None, AR=True)
            else:
                (dim, mod_image) = resize(image, width=int(width), height=int(height), AR=True)
        st.text('The new image dimensions are: ' + str(dim))

    elif selection == IMAGE_NAV_OPTIONS[6]:
        blur_type = st.sidebar.radio('Select the blurring type', ('Average Blur', 'Gaussian Blur', 'Median Blur', 'Bilateral Blur'))
        kernel = st.sidebar.slider('Select the blur intensity', min_value=1, step=2)
        mod_image = blur(image, kernel, blur_type[:-5])
    
    elif selection == IMAGE_NAV_OPTIONS[7]:
        hist_type = st.sidebar.radio('Select the histogram technique', ('Grayscale Histogram', 'Color Histogram'))
        if hist_type == 'Grayscale Histogram':
            plt = hist(image, hist_type[:-10], channels)
        else:
            if channels == 3:
                plt = hist(image, hist_type[:-10], channels)
            else:
                st.warning('The image is in Grayscale Mode, so Color Histogram is not possible!!')
        st.pyplot()
        mod_image = None

    return mod_image