import streamlit as st
import google.generativeai as genai
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="AI YouTube Thumbnail Generator", layout="centered")
st.title("🎬 Free AI YouTube Thumbnail Generator")
st.subheader("Enter your video details to generate a viral thumbnail")

api_key = st.text_input("Enter your Gemini API Key:", type="password")
if api_key:
    genai.configure(api_key=api_key)

# Changed from video upload to text inputs to bypass Google's billing rule
video_title = st.text_input("What is your video title?", placeholder="e.g., I Survived 24 Hours In A Desert")
video_desc = st.text_area("Describe what happens in the video:", placeholder="e.g., I had to find water, build a shelter out of cacti, and avoid scorpions at night.")

if video_title and video_desc and api_key:
    if st.button("🚀 Generate Thumbnail"):
        with st.spinner("Gemini is analyzing your hook and planning the visuals..."):
            
            model = genai.GenerativeModel(model_name="gemini-2.5-flash")
            
            prompt = f"""
            You are an expert YouTube designer. Based on the video title "{video_title}" and description "{video_desc}",
            create a highly descriptive image generation prompt for a YouTube Thumbnail.
            The visual concept must be click-worthy, dramatic, high-contrast, with vibrant colors and clear cinematic framing.
            Return ONLY the text prompt for the image generator, nothing else. Do not include markdown formatting.
            """
            
            response = model.generate_content(prompt)
            thumbnail_prompt = response.text
            
            st.success("✨ Visual Concept Created!")
            
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
