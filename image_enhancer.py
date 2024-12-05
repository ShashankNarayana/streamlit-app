import streamlit as st
import cv2
import numpy as np

st.title("Image Enhancer")
st.write("Upload an image to apply enhancements.")

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    image = cv2.imdecode(file_bytes, 1)
    
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Enhancing image...")
    
    # Example enhancement: convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    st.image(gray_image, caption="Enhanced Image (Grayscale)", use_column_width=True)
