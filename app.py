import streamlit as st
import google.generativeai as genai
import requests
from PIL import Image
from io import BytesIO

# Set up page with a clean, centered layout
st.set_page_config(page_title="VividThumbnail AI Pro", page_icon="🎬", layout="centered")

# Custom CSS to make the UI look premium, cinematic, and lock the 16:9 aspect ratio
st.markdown("""
    <style>
    /* Main App Background Tuning */
    .stApp {
        background-color: #0d0e12;
    }
    
    /* Title Styling */
    .main-title {
        font-family: 'Inter', sans-serif;
        font-weight: 800;
        background: linear-gradient(45deg, #ff4b4b, #ff761b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 5px;
    }
    
    /* Subtitle text colors */
    .sub-text {
        color: #9ca3af;
        text-align: center;
        font-size: 16px;
        margin-bottom: 30px;
    }

    /* Fixed 16:9 Thumbnail Container to completely stop top/bottom compression */
    .thumbnail-frame {
        width: 100%;
        position: relative;
        padding-top: 56.25%; /* Perfect 16:9 Aspect Ratio */
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 0 25px rgba(255, 75, 75, 0.25);
        border: 2px solid #ff4b4b;
        background-color: #1a1c23;
        margin-top: 15px;
        margin-bottom: 20px;
    }
    
    .thumbnail-frame img {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover; /* Forces image to scale perfectly without squeezing */
    }
    
    /* Button Premium Styling */
    div.stButton > button:first-child {
        background: linear-gradient(90deg, #ff4b4b 0%, #ff761b 100%);
        color: white;
        font-weight: bold;
        border: none;
        padding: 12px 30px;
        border-radius: 8px;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255, 75, 75, 0.4);
    }
    div.stButton > button:first-child:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 75, 75, 0.6);
    }
    </style>
""", unsafe_allowed_html=True)

# App UI Header Area
st.markdown("<h1 class='main-title'>🎬 VividThumbnail AI Pro</h1>", unsafe_allowed_html=True)
st.markdown("<p class='sub-text'>Transform reference frames into high-CTR, 20k-style viral masterpieces</p>", unsafe_allowed_html=True)

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

# Main Form Cards
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
                
                # Render the image inside the non-compressible CSS 16:9 Frame
                st.markdown("### 🏆 Your Optimized Production Thumbnail")
                st.markdown(f"""
                    <div class='thumbnail-frame'>
                        <img src='{image_url}' alt='Generated Thumbnail'>
                    </div>
                """, unsafe_allowed_html=True)
                
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
            
