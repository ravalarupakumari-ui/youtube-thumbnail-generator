import streamlit as st
import google.generativeai as genai
import requests
from PIL import Image
from io import BytesIO

# Page setup
st.set_page_config(page_title="VividThumbnail AI Pro", page_icon="🎬", layout="centered")

# App Header
st.title("🎬 VividThumbnail AI Pro")
st.caption("Transform reference frames into high-CTR, viral masterpieces.")
st.markdown("---")

# Clean Sidebar for Settings & Configurations
with st.sidebar:
    st.markdown("### ⚙️ Engine Settings")
    api_key = st.text_input("Gemini API Key:", type="password", help="Paste your free API key from Google AI Studio")
    st.markdown("---")
    st.markdown("### 🎨 Visual Theme")
    style_preference = st.selectbox(
        "Select Thumbnail Target Vibe:",
        [
            "⚡ High-Saturation Gaming (Neon accents, aggressive speedlines, intense glow)",
            "🎬 Dramatic Cinematic (Deep shadows, high-contrast HDR, intense color grading)",
            "📈 Premium Infotainment (Bold flat text, high clarity, clean modern layout)",
            "🔥 Extreme Clickbait (Shocked expressions, glowing outlines, high element depth)"
        ]
    )

if api_key:
    genai.configure(api_key=api_key)

# Main Form inputs
st.markdown("### 📝 Video Presentation")
video_title = st.text_input("Video Title:", placeholder="e.g., Clash Squad Grandmaster Push! 👑")

st.markdown("### 📸 Visual Core Asset")
uploaded_image = st.file_uploader("Upload a reference screenshot or character cutout:", type=["jpg", "jpeg", "png"])

# Display reference beautifully if loaded
if uploaded_image:
    ref_image = Image.open(uploaded_image)
    with st.expander("🖼️ View Uploaded Reference Frame", expanded=True):
        st.image(ref_image, use_container_width=True)

# Generation logic
if video_title and uploaded_image and api_key:
    st.markdown("<br>", unsafe_allowed_html=True)
    if st.button("🚀 GENERATE 20K WORTHY THUMBNAIL"):
        
        with st.spinner("⚡ Step 1: Gemini is extracting visual subjects and tracking composition hooks..."):
            model = genai.GenerativeModel(model_name="gemini-2.5-flash")
            
            prompt = f"""
            Analyze the provided reference image and the video title: "{video_title}".
            You are a legendary YouTube graphic designer making thumbnails that pull millions of views.
            Based on the image structure, create a highly detailed image generation prompt.
            The style must be: {style_preference}.
            Specify intense highlights, razor-sharp foreground details, clean composition depth, vibrant colors, and cinematic presentation.
            Return ONLY the raw descriptive prompt text. No intros, no conversational fillers, no markdown formatting.
            """
            
            response = model.generate_content([ref_image, prompt])
            thumbnail_prompt = response.text
            
        with st.spinner("🎨 Step 2: Rendering widescreen layout canvas..."):
            encoded_prompt = requests.utils.quote(thumbnail_prompt)
            image_url = f"https://image.pollinations.ai/p/{encoded_prompt}?width=1280&height=720&enhance=true"
            img_response = requests.get(image_url)
            
            if img_response.status_code == 200:
                img = Image.open(BytesIO(img_response.content))
                
                # Convert image to bytes for the download engine
                buf = BytesIO()
                img.save(buf, format="JPEG")
                byte_im = buf.getvalue()
                
                st.markdown("### 🏆 Your Optimized Production Thumbnail")
                
                # Native container width scaling to prevent top/bottom compression completely
                st.image(img, use_container_width=True, caption="Final Rendered Concept (16:9 Cinema Aspect)")
                
                # High-visibility Download Button
                st.download_button(
                    label="📥 DOWNLOAD ULTRA-HD THUMBNAIL (16:9)", 
                    data=byte_im, 
                    file_name="viral_thumbnail.jpg", 
                    mime="image/jpeg"
                )
            else:
                st.error("Rerouting generation request failed. Please tap the button again to recreate!")
else:
    if not api_key:
        st.info("💡 Quick Start: Add your Gemini API Key in the left sidebar configuration to activate the engine.")
            
