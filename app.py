import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import io

# Title and description
st.title("Image Enhancer")
st.write("This is a basic app for image enhancement using Streamlit.")

# Email configuration (replace with your email details)
EMAIL_ADDRESS = 'your_email@gmail.com'  # Replace with your email
EMAIL_PASSWORD = 'your_email_password'  # Replace with your email password

def send_email(subject, body, to_email, attachment):
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(body)

    # Attach the file
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment)
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename={attachment.name}")
    msg.attach(part)

    # Send email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    text = msg.as_string()
    server.sendmail(EMAIL_ADDRESS, to_email, text)
    server.quit()

# Image upload feature
uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    # Open the uploaded image using PIL
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Grayscale conversion
    if st.button("Convert to Grayscale"):
        gray_image = image.convert("L")
        st.image(gray_image, caption="Grayscale Image", use_column_width=True)

    # Image Enhancement (Sharpening)
    if st.button("Enhance Image (Sharpen)"):
        enhancer = ImageEnhance.Sharpness(image)
        enhanced_image = enhancer.enhance(2.0)  # Enhance sharpness by a factor of 2
        st.image(enhanced_image, caption="Enhanced Image", use_column_width=True)

    # Image Denoising (Gaussian Blur)
    if st.button("Denoise Image (Gaussian Blur)"):
        denoised_image = image.filter(ImageFilter.GaussianBlur(radius=2))  # Apply Gaussian blur
        st.image(denoised_image, caption="Denoised Image", use_column_width=True)

    # Digital Signal Processing (Fourier Transform)
    if st.button("Convert Image to DSP (Fourier Transform)"):
        img_array = np.array(image)
        # Convert the image to grayscale for processing
        gray_img = np.mean(img_array, axis=2)
        # Perform the Fourier Transform
        f_transform = np.fft.fft2(gray_img)
        f_transform_shifted = np.fft.fftshift(f_transform)
        magnitude_spectrum = np.abs(f_transform_shifted)

        st.image(magnitude_spectrum, caption="Fourier Transform Magnitude Spectrum", use_column_width=True)

    # Email functionality
    email = st.text_input("Enter your email address to receive the processed image:")

    if email and st.button("Send Processed Image"):
        # Get the processed image (for example, grayscale image)
        image_bytes = io.BytesIO()
        gray_image.save(image_bytes, format='JPEG')
        image_bytes.seek(0)
        # Send the email with the image as attachment
        send_email("Your Processed Image", "Here is your processed image.", email, image_bytes)
        st.success("Email sent successfully!")
