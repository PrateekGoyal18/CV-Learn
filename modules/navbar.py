import streamlit as st
from modules.opencv import extract, shift, rotate, rotate_bound

def navbar(image, selection):
    if selection == 'Color Extraction':
        color = st.sidebar.radio("Select the color you want to extract",
            ('Red', 'Blue', 'Green'))
        mod_image = extract(image, color)

    elif selection == 'Shifting':
        x = st.sidebar.slider('Select the x-axis value',
            0, image.shape[1])
        y = st.sidebar.slider('Select the y-axis value',
            0, image.shape[0])
        mod_image = shift(image, x, y)

    elif selection == 'Rotation':
        rotate_type = st.sidebar.radio("Select the sub-feature",
            ('Basic Rotation', 'Bound Rotation'))
        if rotate_type == 'Basic Rotation':
            angle = st.sidebar.slider('Select an angle',
                -360.0, 360.0)
            mod_image = rotate(image, angle)
        else:
            angle = st.sidebar.slider('Select an angle',
                -360.0, 360.0)
            mod_image = rotate_bound(image, angle)

    elif selection == 'Resize':
        resize_type = st.sidebar.radio("Select the sub-feature",
            ('Without Aspect Ratio', 'With Aspect Ratio'))
        if resize_type == 'Without Aspect Ratio':
            width = st.sidebar.number_input('Enter the width:')
            height = st.sidebar.number_input('Enter the height:')
        else:
            width = st.sidebar.input()
            height = st.sidebar.input()

    return mod_image