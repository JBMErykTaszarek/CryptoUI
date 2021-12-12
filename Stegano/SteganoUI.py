import streamlit as st
from PIL import Image
import cv2
import numpy as np
import VC.Services.PixelProcessing as pp

def SteganoUI():
    if st.button("dupa"):
        originalImage = Image.open('Stegano/ok.png')
        sequence_of_pixels = originalImage.getdata()
        outputImage = list(sequence_of_pixels)
        print(outputImage)
        message = "ok" #0110101
        a_byte_array = bytearray(message, "utf8")
        binaryChars = []
        for byte in a_byte_array:
            binary_representation = bin(byte)
            binaryChars.append(binary_representation)
        print(binaryChars)
        k = []
        for elem in binaryChars:
            k.append(elem[2:])
        print("".join(k))
        cnt = 0
        newBitMap = []
