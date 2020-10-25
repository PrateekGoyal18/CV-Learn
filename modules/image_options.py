import streamlit as st
from streamlit_cropper import st_cropper
from modules.image_functions import *
from modules.vars import *
import pandas as pd

def image_op(image, channels, selection):
    if selection == IMAGE_NAV_OPTIONS[0]:
        if channels == 3:
            channels = str(3) + ' (RGB)'
        else:
            channels = str(1) + ' (Grayscale)'
        st.markdown('''<div class="image-info">
            <div class="section">Height/Rows: ''' + str(image.shape[0]) + '''px</div>
            <div class="section">Width/Columns: ''' + str(image.shape[1]) + '''px</div>
            <div class="section">Channels: ''' + channels + '''</div>
            </div>''', unsafe_allow_html=True)
        mod_image = None
        ch = None

    elif selection == IMAGE_NAV_OPTIONS[1]:
        crop_type = st.sidebar.radio("Select the sub-feature", ('Draw on the image', 'With dimensions'))
        if crop_type == 'Draw on the image':
            realtime_update = st.sidebar.checkbox(label="Update in Real Time", value=True)
            box_color = st.sidebar.beta_color_picker(label="Box Color", value='#0000FF')
            aspect_choice = st.sidebar.radio(label="Aspect Ratio", options=["1:1", "16:9", "4:3", "2:3", "Free"])
            aspect_dict = {"1:1": (1,1),
                            "16:9": (16,9),
                            "4:3": (4,3),
                            "2:3": (2,3),
                            "Free": None}
            aspect_ratio = aspect_dict[aspect_choice]
            # if image:
                # img = Image.open(image)
            if not realtime_update:
                st.write("Double click to save crop")
                # Get a cropped image from the frontend
                mod_image = st_cropper(image, realtime_update=realtime_update, box_color=box_color,
                                aspect_ratio=aspect_ratio)
        else:
            x = st.sidebar.slider('Select the x-axis value', 0, image.shape[1], (0, image.shape[1]))
            y = st.sidebar.slider('Select the y-axis value', 0, image.shape[0], (0, image.shape[0]))
            mod_image = image[y[0]:y[1], x[0]:x[1]]
        ch = 3

    elif selection == IMAGE_NAV_OPTIONS[2]:
        if channels == 3:
            mod_image = grayscale(image)
        else:
            st.warning('The image is already in Grayscale Mode!!')
            mod_image = None
        ch = 1

    elif selection == IMAGE_NAV_OPTIONS[3]:
        # clicked = False
        # r = g = b = xpos = ypos = 0
        # index = ["color", "color_name", "hex", "R", "G", "B"]
        # csv = pd.read_csv('assets/colors.csv', names=index, header=None)
        # cv2.setMouseCallback('image', draw_function)
        # if (clicked):
        #     #cv2.rectangle(image, startpoint, endpoint, color, thickness)-1 fills entire rectangle 
        #     cv2.rectangle(image, (20,20), (750,60), (b,g,r), -1)

        #     #Creating text string to display( Color name and RGB values )
        #     text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
            
        #     #cv2.putText(img,text,start,font(0-7),fontScale,color,thickness,lineType )
        #     # cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)

        #     #For very light colours we will display text in black colour
        #     # if(r+g+b>=600):
        #         # cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        #     st.text(text)
        #     clicked=False
        mod_image = None
        ch = None

    elif selection == IMAGE_NAV_OPTIONS[4]:
        if channels == 3:
            color = st.sidebar.radio("Select the color you want to extract", ('Red', 'Blue', 'Green'))
            mod_image = extract(image, color)
        else:
            st.warning('The image is not in RGB format!!')
            mod_image = None
        ch = 3

    elif selection == IMAGE_NAV_OPTIONS[5]:
        x = st.sidebar.slider('Select the x-axis value', 0, image.shape[1])
        y = st.sidebar.slider('Select the y-axis value', 0, image.shape[0])
        mod_image = shift(image, x, y)
        ch = 3

    elif selection == IMAGE_NAV_OPTIONS[6]:
        rotate_type = st.sidebar.radio("Select the sub-feature", ('Basic Rotation', 'Bound Rotation'))
        if rotate_type == 'Basic Rotation':
            angle = st.sidebar.slider('Select an angle', -360.0, 360.0)
            mod_image = rotate(image, angle, bound=False)
        else:
            angle = st.sidebar.slider('Select an angle', -360.0, 360.0)
            mod_image = rotate(image, angle, bound=True)
        ch = 3

    elif selection == IMAGE_NAV_OPTIONS[7]:
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
        ch = 3

    elif selection == IMAGE_NAV_OPTIONS[8]:
        blur_type = st.sidebar.radio('Select the blurring type', ('Average Blur', 'Gaussian Blur', 'Median Blur', 'Bilateral Blur'))
        kernel = st.sidebar.slider('Select the blur intensity', min_value=1, step=2)
        mod_image = blur(image, kernel, blur_type[:-5])
        ch = 3
    
    elif selection == IMAGE_NAV_OPTIONS[9]:
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
        ch = None

    elif selection == IMAGE_NAV_OPTIONS[10]:
        cartoon_type = st.sidebar.radio('Select the cartoonization technique', ('Pencil Sketch', 'Detail Enhancement', 'Pencil Edges', 'Bilateral Filter'))
        mod_image, ch = cartoonization(image, cartoon_type)

    return mod_image, ch