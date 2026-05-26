import streamlit as st
from PIL import Image
import urllib.parse

# Page configuration
st.set_page_config(page_title="VividThumbnail Pro Studio", page_icon="🔥", layout="centered")

# Your updated WhatsApp Business Number
YOUR_WHATSAPP_NUMBER = "919848887073" 

# Custom Dark Cinematic Header
st.title("🔥 VividThumbnail Pro Studio")
st.markdown("""
    <h3 style='color: #ff4b4b; margin-top: -15px;'>Where Viral Concepts Are Made Manually</h3>
    <p style='color: #9ca3af;'>Skip the basic AI templates. Get a custom, high-CTR thumbnail engineered by a professional designer to dominate the algorithm.</p>
    <hr style='border-color: #262730;'>
""", unsafe_allowed_html=True)

# Client Inputs
st.markdown("### 📝 Step 1: Video Presentation")
video_title = st.text_input("What is your Video Title?", placeholder="e.g., Clash Squad Grandmaster Push! 👑")

style_preference = st.selectbox(
    "Select Your Visual Vibe:",
    [
        "⚡ High-Saturation Gaming (Neon accents, intense glow)",
        "🎬 Dramatic Cinematic (Deep shadows, high-contrast HDR)",
        "📈 Premium Infotainment (Bold text, clean layout)",
        "🔥 Extreme Clickbait (Aggressive depth, glowing outlines)"
    ]
)

st.markdown("### 📸 Step 2: Visual Assets")
uploaded_image = st.file_uploader("Upload your raw screenshot, character cutout, or background scene:", type=["jpg", "jpeg", "png"])

if uploaded_image:
    ref_image = Image.open(uploaded_image)
    with st.expander("🖼️ Review Uploaded Asset", expanded=True):
        st.image(ref_image, use_column_width="always")

st.markdown("---")

# Order Processing Block
if video_title and uploaded_image:
    st.markdown("### 🚀 Step 3: Secure Your Design Slot")
    
    # Premium Elite Hook Display Box
    st.info("""
        ⚡ **AI can't beat human psychology.** Your asset is being handed over to an elite cinematic designer. 
        Your custom high-CTR layout is being crafted manually and will hit your inbox within 24 hours.
    """)
    
    # Pre-filled chat message template
    raw_message = f"""👋 Hello VividThumbnail Studio! I want to order a premium thumbnail.

📝 VIDEO DETAILS:
• Title: {video_title}
• Vibe/Style: {style_preference}

🖼️ NOTE: I have uploaded my reference image on the portal and am sending it along over chat now!"""

    # Encode message safely for URLs
    encoded_message = urllib.parse.quote(raw_message)
    whatsapp_url = f"https://wa.me/{YOUR_WHATSAPP_NUMBER}?text={encoded_message}"
    
    # CTA Order Button with WhatsApp branding
    st.markdown(f"""
        <a href="{whatsapp_url}" target="_blank" style="text-decoration: none;">
            <button style="
                background: linear-gradient(90deg, #25D366 0%, #128C7E 100%);
                color: white;
                font-weight: bold;
                font-size: 18px;
                border: none;
                padding: 15px 30px;
                border-radius: 8px;
                width: 100%;
                cursor: pointer;
                box-shadow: 0 4px 15px rgba(37, 211, 102, 0.4);
                transition: transform 0.2s;">
                💬 SUBMIT ORDER VIA WHATSAPP
            </button>
        </a>
    """, unsafe_allowed_html=True)
    
    st.caption("👉 Clicking the green button opens WhatsApp instantly. Make sure to attach your uploaded image to the chat window so I can download it in full quality!")

else:
    st.warning("💡 Fill out your Video Title and upload a reference photo above to activate your order funnel.")
    
