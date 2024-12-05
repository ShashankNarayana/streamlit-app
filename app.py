import streamlit as st
import numpy as np
import cv2
from PIL import Image

# Function to process the uploaded image
def process_image(image):
    # Convert the uploaded image to a numpy array
    img = np.array(image)
    
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # Perform Fourier Transform (shifted)
    f = np.fft.fft2(gray_image)
    fshift = np.fft.fftshift(f)
    
    # Compute the magnitude spectrum
    magnitude_spectrum = np.abs(fshift)
    
    # Normalize the magnitude spectrum to be in the range [0, 1]
    magnitude_spectrum = np.log(magnitude_spectrum + 1)  # Add 1 to avoid log(0)
    magnitude_spectrum = cv2.normalize(magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX)
    magnitude_spectrum = np.uint8(magnitude_spectrum)  # Convert to uint8 for display
    
    return gray_image, magnitude_spectrum

# Streamlit interface
st.title("Image Processing with Fourier Transform")

# Upload an image
uploaded_file = st.file_uploader("Upload an Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    
    # Display the original image
    st.image(image, caption="Original Image", use_column_width=True)
    
    # Process the image
    gray_image, magnitude_spectrum = process_image(image)
    
    # Display the grayscale image
    st.image(gray_image, caption="Grayscale Image", use_column_width=True, channels="GRAY")
    
    # Display the magnitude spectrum
    st.image(magnitude_spectrum, caption="Fourier Transform Magnitude Spectrum", use_column_width=True)

    # Option to download the image
    st.download_button(
        label="Download Processed Image (Magnitude Spectrum)",
        data=magnitude_spectrum.tobytes(),  # Convert the processed image to byte format
        file_name="magnitude_spectrum.png",
        mime="image/png",
    )
