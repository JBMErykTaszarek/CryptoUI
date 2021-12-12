import streamlit as st
from PIL import Image
import cv2
import numpy as np
import VC.Services.PixelProcessing as pp

def VcUi():
    originalImage = cv2.imread('VC/Secret.png')
    st.write("zdjęcie orginalne")
    st.image(originalImage)
    if st.button("generate"):
        grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
        (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
        cv2.imshow('Black white image', blackAndWhiteImage)
        cv2.imwrite("C:/Users/erykt/PycharmProjects/CryptoUI/VC/BWSecret.jpg", blackAndWhiteImage)
        share1 = []
        share2 = []
        for line in blackAndWhiteImage:
            line1 = []
            line2 = []
            for pixel in line:
                if pixel == 255:
                    if(pp.randomPixelChoose()):
                        line1.append((0,0,0))
                        line1.append((255,255,255))
                        line2.append((0, 0, 0))
                        line2.append((255, 255, 255))
                    else:
                        line1.append((255, 255, 255))
                        line1.append((0, 0, 0))
                        line2.append((255, 255, 255))
                        line2.append((0, 0, 0))
                if pixel == 0:
                    if (pp.randomPixelChoose()):
                        line1.append((0, 0, 0))
                        line1.append((255, 255, 255))
                        line2.append((255, 255, 255))
                        line2.append((0, 0, 0))
                    else:
                        line1.append((255, 255, 255))
                        line1.append((0, 0, 0))
                        line2.append((0, 0, 0))
                        line2.append((255, 255, 255))
            share1.append(line1)
            share2.append(line2)

        array = np.array(share1, dtype=np.uint8)
        new_image = Image.fromarray(array)
        new_image.save("C:/Users/erykt/PycharmProjects/CryptoUI/VC/Share1.jpg")
        st.write("Udział nr 1")
        st.image(new_image)


        array = np.array(share2, dtype=np.uint8)
        new_image = Image.fromarray(array)
        new_image.save("C:/Users/erykt/PycharmProjects/CryptoUI/VC/Share2.jpg")
        st.write("Udział nr 2")
        st.image(new_image)

        merged = []
        for line1, line2 in zip(share1, share2):
            mergedLine = []
            for pixel1, pixel2 in zip(line1, line2):
                if pixel1 == (255,255,255) and pixel2 == (255,255,255):
                    mergedLine.append((255,255,255))
                else:
                    mergedLine.append((0,0,0))
            merged.append(mergedLine)
        array = np.array(merged, dtype=np.uint8)
        new_image = Image.fromarray(array)
        new_image.save("C:/Users/erykt/PycharmProjects/CryptoUI/VC/Merged.jpg")
        st.write("Zdjęcie wyjściowe (nałożone na siebie udziały)")
        st.image(new_image)
