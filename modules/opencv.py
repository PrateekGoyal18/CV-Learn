import cv2
import numpy as np

def grayscale(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray

def extract(image, color):
    (B, G, R) = cv2.split(image)
    zeros = np.zeros(image.shape[:2], dtype="uint8")
    if color.lower() == 'red' or color.lower() == 'r':
        return cv2.merge([zeros, zeros, R])
    elif color.lower() == 'green' or color.lower() == 'g':
        return cv2.merge([zeros, G, zeros])
    else:
        return cv2.merge([B, zeros, zeros])

def shift(image, x, y):
    M = np.float32([[1, 0, x], [0, 1, y]])
    shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    return shifted

def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    if center is None:
        center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
    return rotated

def rotate_bound(image, angle):
    (h, w) = image.shape[:2]
    (cX, cY) = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D((cX, cY), -angle, 1.0)
    cos = np.abs(M[0, 0])
    sin = np.abs(M[0, 1])
    nW = int((h * sin) + (w * cos))
    nH = int((h * cos) + (w * sin))
    M[0, 2] += (nW / 2) - cX
    M[1, 2] += (nH / 2) - cY
    rotated_bound = cv2.warpAffine(image, M, (nW, nH))
    return rotated_bound

def resize_woAR(image, width=None, height=None, inter=cv2.INTER_AREA):
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        dim = (w, height)
    elif height is None:
        dim = (width, h)
    else:
        dim = (width, height)
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized

def resize_wAR(image, width=None, height=None, inter=cv2.INTER_AREA):
    (h, w) = image.shape[:2]
    if width is None and height is None:
        return image
    if width is None:
        r = height/float(h)
        dim = (int(w*r), height)
    else:
        r = width/float(w)
        dim = (width, int(h*r))
    resized = cv2.resize(image, dim, interpolation=inter)
    return resized

def rectMask(image):
    (cX, cY) = (image.shape[1]//2, image.shape[0]//2)
    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.rectangle(mask, (cX-75, cY-75), (cX+75, cY+75), 255, -1)
    masked = cv2.bitwise_and(image, image, mask=mask)
    return masked

def cirMask(image):
    (cX, cY) = (image.shape[1]//2, image.shape[0]//2)
    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.circle(mask_cir, (cX, cY), 100, 255, -1)
    masked = cv2.bitwise_and(image, image, mask=mask)
    return masked

def addition(image, value):
    M = np.ones(image.shape, dtype="uint8")*value
    added = cv2.add(image, M)
    return added

def subtraction(image, value):
    M = np.ones(image.shape, dtype="uint8")*value
    subtracted = cv2.subtract(image, M)
    return subtracted