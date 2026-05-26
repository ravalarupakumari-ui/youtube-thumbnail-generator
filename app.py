import streamlit as st
import google.generativeai as genai
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="AI Pro Thumbnail Generator", layout="centered")
st.title("🔥 AI Pro 20k-Style Thumbnail Generator")
st.subheader("Combine your title and a reference photo to create a high-CTR viral thumbnail")

api_key = st.text_input("Enter your Gemini API Key:", type="password")
if api_key:
    genai.configure(api_key=api_key)

# Inputs for high-value thumbnail context
video_title = st.text_input("What is your video title?", placeholder="e.g., Clash Squad Grandmaster Push! 👑")
style_preference = st.selectbox(
    "Choose Thumbnail Visual Style:",
    ["Cinematic & Moody", "High-Saturation Gaming (Neon accents, intense lighting)", "Clean & Professional (Modern, bold typography)", "Dramatic / Shocking (High contrast, aggressive depth)"]
)

# Reference photo uploader (Images are FREE on Gemini API)
uploaded_image = st.file_uploader("Upload a reference photo (Screenshot, face cutout, or background scene):", type=["jpg", "jpeg", "png"])

if uploaded_image:
    # Display the uploaded reference image in the UI
    ref_image = Image.open(uploaded_image)
    st.image(ref_image, caption="Your Reference Photo", width=300)

if video_title and uploaded_image and api_key:
    if st.button("🚀 Generate Pro Thumbnail"):
        with st.spinner("Gemini is analyzing your reference photo and designing the composition..."):
            
            # Using the fast, multimodal flash model to read both text and image
            model = genai.GenerativeModel(model_name="gemini-2.5-flash")
            
            prompt = f"""
            Analyze the provided reference image and the video title: "{video_title}".
            You are a world-class YouTube thumbnail designer who creates 20k-value viral graphics.
            Design a brand new thumbnail concept that heavily builds on the elements, subject, or mood of the reference image.
            
            The style must be: {style_preference}.
            Create a highly detailed, descriptive image generation prompt for this thumbnail. 
            Specify aggressive foreground lighting, cinematic background depth, intense color grading, and a composition designed to catch eyes instantly.
            
            Return ONLY the detailed text prompt for the image generator. Do not include any introductory remarks or markdown formatting.
            """
            
            # Pass both the uploaded image object and the text prompt to Gemini
            response = model.generate_content([ref_image, prompt])
            thumbnail_prompt = response.text
            
        with st.spinner("Rendering your high-value thumbnail..."):
            encoded_prompt = requests.utils.quote(thumbnail_prompt)
            # Fetching the high-quality, enhanced image layout from the free engine
            image_url = f"https://image.pollinations.ai/p/{encoded_prompt}?width=1280&height=720&enhance=true"
            img_response = requests.get(image_url)
            
            if img_response.status_code == 200:
                img = Image.open(BytesIO(img_response.content))
                st.image(img, caption="Your Generated YouTube Thumbnail (16:9)", use_container_width=True)
                
                buf = BytesIO()
                img.save(buf, format="JPEG")
                byte_im = buf.getvalue()
                st.download_button(label="📥 Download Pro Thumbnail", data=byte_im, file_name="pro_thumbnail.jpg", mime="image/jpeg")
            else:
                st.error("Failed to render image. Please try pressing the button again!")
            
