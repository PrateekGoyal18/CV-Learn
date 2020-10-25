import cv2
import numpy as np
from matplotlib import pyplot as plt
import streamlit as st

# Image BGR to Grayscale
def grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

# Color Extraction
def extract(image, color):
    (B, G, R) = cv2.split(image)
    zeros = np.zeros(image.shape[:2], dtype="uint8")
    if color.lower() == 'red' or color.lower() == 'r':
        return cv2.merge([zeros, zeros, R])
    elif color.lower() == 'green' or color.lower() == 'g':
        return cv2.merge([zeros, G, zeros])
    else:
        return cv2.merge([B, zeros, zeros])

# Image Shifting
def shift(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

# Image Rotation
def rotate(image, angle, center=None, scale=1.0, bound=False):
    (h, w) = image.shape[:2]
    if bound == False:
        if center is None:
            center = (w // 2, h // 2)
        M = cv2.getRotationMatrix2D(center, angle, scale)
        rotated = cv2.warpAffine(image, M, (w, h))
    else:
        (cX, cY) = (w / 2, h / 2)
        M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
        cos = np.abs(M[0, 0])
        sin = np.abs(M[0, 1])
        nW = int((h * sin) + (w * cos))
        nH = int((h * cos) + (w * sin))
        M[0, 2] += (nW / 2) - cX
        M[1, 2] += (nH / 2) - cY
        rotated = cv2.warpAffine(image, M, (nW, nH))
    return rotated

# Image Resizing
def resize(image, width=None, height=None, inter=cv2.INTER_AREA, AR=False):
    (h, w) = image.shape[:2]
    if AR == False:
        if width is None and height is None:
            resized = image
        elif width is None:
            dim = (w, height)
        elif height is None:
            dim = (width, h)
        else:
            dim = (width, height)
        resized = cv2.resize(image, dim, interpolation=inter)
    else:
        if width is None and height is None:
            resized = image
        elif width is None:
            r = height/float(h)
            dim = (int(w*r), height)
        else:
            r = width/float(w)
            dim = (width, int(h*r))
        resized = cv2.resize(image, dim, interpolation=inter)
    return dim, resized

# Blurring Techniques
def blur(image, kernel, blur_type):
    if blur_type == 'Average':
        blurred = cv2.blur(image, (kernel,kernel))
    elif blur_type == 'Gaussian':
        blurred = cv2.GaussianBlur(image, (kernel,kernel), 0)
    elif blur_type == 'Median':
        blurred = cv2.medianBlur(image, kernel)
    return blurred

# Grayscale and Color Histogram
def hist(image, hist_type, channels):
    if hist_type == 'Grayscale':
        if channels == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image
        hist = cv2.calcHist(images=[gray], channels=[0], mask=None, histSize=[256], ranges=[0,256])
        plt.figure()
        plt.title("Grayscale Histogram")
        plt.xlabel("Intensities")
        plt.ylabel("No. of Pixels")
        plt.plot(hist)
        plt.xlim([0, 256])
    else:
        chans = cv2.split(image)
        colors = ("b", "g", "r")
        plt.figure()
        plt.title("Color Histogram")
        plt.xlabel("Intensities")
        plt.ylabel("No. of Pixels")
        for (chan, color) in zip(chans, colors):
            hist = cv2.calcHist(images=[chan], channels=[0], mask=None, histSize=[256], ranges=[0,256])
            plt.plot(hist, color=color)
            plt.xlim([0, 256])
    return plt

# Masking
def mask(image, mask_type):
    (cX, cY) = (image.shape[1]//2, image.shape[0]//2)
    mask = np.zeros(image.shape[:2], dtype="uint8")
    if rect in mask_type:
        cv2.rectangle(mask, (cX-75, cY-75), (cX+75, cY+75), 255, -1)
    elif cir in mask_type:
        cv2.circle(mask_cir, (cX, cY), 100, 255, -1)
    masked = cv2.bitwise_and(image, image, mask=mask)
    return masked

# Arithmetic Operations
def arithmetic_op(image, value, operator):
    M = np.ones(image.shape, dtype="uint8")*value
    if add in operator:
        arithmetic = cv2.add(image, M)
    elif sub in operator:
        arithmetic = cv2.subtract(image, M)
    return arithmetic

# Cartoonization
def cartoonization (img, cartoon):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    if cartoon == "Pencil Sketch":
        value = st.sidebar.slider('Tune the brightness of your sketch (the higher the value, the brighter your sketch)', 0.0, 300.0, 250.0)
        kernel = st.sidebar.slider('Tune the boldness of the edges of your sketch (the higher the value, the bolder the edges)', 1, 99, 25, step=2)
        gray_blur = cv2.GaussianBlur(gray, (kernel, kernel), 0)
        cartoon = cv2.divide(gray, gray_blur, scale=value)
        channels = 1

    elif cartoon == "Detail Enhancement":
        smooth = st.sidebar.slider('Tune the smoothness level of the image (the higher the value, the smoother the image)', 3, 99, 5, step=2)
        kernel = st.sidebar.slider('Tune the sharpness of the image (the lower the value, the sharper it is)', 1, 21, 3, step=2)
        edge_preserve = st.sidebar.slider('Tune the color averaging effects (low: only similar colors will be smoothed, high: dissimilar color will be smoothed)', 0.0, 1.0, 0.5)
        gray = cv2.medianBlur(gray, kernel) 
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9) 
        color = cv2.detailEnhance(img, sigma_s=smooth, sigma_r=edge_preserve)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        channels = 3

    elif cartoon == "Pencil Edges":
        kernel = st.sidebar.slider('Tune the sharpness of the sketch (the lower the value, the sharper it is)', 1, 99, 25, step=2)
        laplacian_filter = st.sidebar.slider('Tune the edge detection power (the higher the value, the more powerful it is)', 3, 9, 3, step =2)
        noise_reduction = st.sidebar.slider('Tune the noise effects of your sketch (the higher the value, the noisier it is)', 10, 255, 150)
        gray = cv2.medianBlur(gray, kernel) 
        edges = cv2.Laplacian(gray, -1, ksize=laplacian_filter)
        edges_inv = 255-edges
        dummy, cartoon = cv2.threshold(edges_inv, noise_reduction, 255, cv2.THRESH_BINARY)
        channels = 1
        
    elif cartoon == "Bilateral Filter":
        smooth = st.sidebar.slider('Tune the smoothness level of the image (the higher the value, the smoother the image)', 3, 99, 5, step=2)
        kernel = st.sidebar.slider('Tune the sharpness of the image (the lower the value, the sharper it is)', 1, 21, 3, step =2)
        edge_preserve = st.sidebar.slider('Tune the color averaging effects (low: only similar colors will be smoothed, high: dissimilar color will be smoothed)', 1, 100, 50)
        gray = cv2.medianBlur(gray, kernel) 
        edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
        color = cv2.bilateralFilter(img, smooth, edge_preserve, smooth) 
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        channels = 3 
    return cartoon, channels