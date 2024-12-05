import streamlit as st
from PIL import Image
import io

# Title and description
st.title("Image Enhancer")
st.write("This is a basic app for image enhancement using Streamlit.")

# Image upload feature
uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    # Open the uploaded image using PIL
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Example enhancement: Convert to grayscale
    if st.button("Convert to Grayscale"):
        gray_image = image.convert("L")
        st.image(gray_image, caption="Grayscale Image", use_column_width=True)

