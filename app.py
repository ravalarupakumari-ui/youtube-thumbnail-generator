import streamlit as st
import google.generativeai as genai
import requests
from PIL import Image
from io import BytesIO
import os

st.set_page_config(page_title="AI YouTube Thumbnail Generator", layout="centered")
st.title("🎬 Free AI YouTube Thumbnail Generator")
st.subheader("Upload your Short or Video to generate a viral thumbnail")

api_key = st.text_input("Enter your Gemini API Key:", type="password")
if api_key:
    genai.configure(api_key=api_key)

uploaded_video = st.file_uploader("Upload your video file (.mp4, .mov)", type=["mp4", "mov"])

if uploaded_video and api_key:
    st.video(uploaded_video)
    
    if st.button("🚀 Analyze Video & Generate Thumbnail"):
        with st.spinner("Gemini is analyzing your video scenes and core hook..."):
            with open("temp_video.mp4", "wb") as f:
                f.write(uploaded_video.read())
                
            video_file = genai.upload_file(path="temp_video.mp4")
            model = genai.GenerativeModel(model_name="gemini-2.5-flash")
            prompt = """
            Analyze this video or YouTube Short. Identify the most exciting, emotional, or shocking moment. 
            Create a highly descriptive image generation prompt for a YouTube Thumbnail based on it.
            The prompt must imply high-contrast, viral-style framing, vibrant colors, and cinematic lighting. 
            Return ONLY the text prompt for the image generator, nothing else.
            """
            response = model.generate_content([video_file, prompt])
            thumbnail_prompt = response.text
            
            st.success("✨ Video Analysis Complete!")
            st.write(f"**Generated Concept:** {thumbnail_prompt}")
            
        with st.spinner("Generating viral thumbnail image..."):
            encoded_prompt = requests.utils.quote(thumbnail_prompt)
            image_url = f"https://image.pollinations.ai/p/{encoded_prompt}?width=1280&height=720&enhance=true"
            img_response = requests.get(image_url)
            
            if img_response.status_code == 200:
                img = Image.open(BytesIO(img_response.content))
                st.image(img, caption="Your Generated YouTube Thumbnail (16:9)", use_container_width=True)
                
                buf = BytesIO()
                img.save(buf, format="JPEG")
                byte_im = buf.getvalue()
                st.download_button(label="📥 Download Thumbnail", data=byte_im, file_name="thumbnail.jpg", mime="image/jpeg")
            else:
                st.error("Failed to generate image. Try again!")
                
        os.remove("temp_video.mp4")
      
