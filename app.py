import streamlit as st
from PIL import Image
import urllib.parse

# Your direct GitHub raw image link for the home screen icon
LOGO_URL = "https://raw.githubusercontent.com/ravalarupakumari-ui/youtube-thumbnail-generator/main/logo.png"

# Page configuration - Locks your custom logo image as the app icon
st.set_page_config(
    page_title="VividThumbnail Pro Studio", 
    page_icon=LOGO_URL, 
    layout="centered"
)

# Your WhatsApp Business Number (91 for India)
YOUR_WHATSAPP_NUMBER = "919848887073" 

# Highlight Banner for Mobile Users to see the sidebar settings toggle
st.warning("👉 MOBILE USERS: Tap the small double arrows ( ☰ or ❯ ) in the upper left corner to adjust configurations!")

# Native App Header
st.title("🔥 VividThumbnail Pro Studio")
st.subheader("Where Viral Concepts Are Made Manually")
st.caption("Skip basic templates. Get a custom, high-CTR thumbnail engineered by a professional designer to dominate the algorithm.")
st.markdown("---")

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

🖼️ REMINDER: Sending my reference image right below this text!"""

    # Encode message safely for URLs
    encoded_message = urllib.parse.quote(raw_message)
    whatsapp_url = f"https://wa.me/{YOUR_WHATSAPP_NUMBER}?text={encoded_message}"
    
    # High-visibility Link Button
    st.link_button("💬 SUBMIT ORDER VIA WHATSAPP", whatsapp_url, use_container_width=True)
    
    st.caption("💡 Note: Clicking the button launches your WhatsApp chat instantly. Simply press send on the pre-filled text, then tap the attachment icon to send over your reference image in full resolution!")

else:
    st.warning("💡 Fill out your Video Title and upload a reference photo above to activate your order funnel.")
    
