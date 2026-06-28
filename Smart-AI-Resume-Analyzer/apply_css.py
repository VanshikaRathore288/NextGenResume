import os

if os.path.exists('style/style.css'):
    with open('style/style.css', 'r', encoding='utf-8') as f:
        original_css = f.read()

new_css = """
/* --- NEW GLASSMORPHISM & NEON THEME --- */
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

/* Global Animated Background */
.stApp {
    font-family: 'Outfit', sans-serif !important;
    background: linear-gradient(-45deg, #09090e, #1a0b2e, #0b1e36, #09090e) !important;
    background-size: 400% 400% !important;
    animation: gradientBG 15s ease infinite !important;
}

@keyframes gradientBG {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Glassmorphism for Streamlit Default Cards */
div[data-testid="stExpander"], div[data-testid="stForm"], .css-1r6slb0 {
    background: rgba(255, 255, 255, 0.03) !important;
    backdrop-filter: blur(16px) !important;
    -webkit-backdrop-filter: blur(16px) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 20px !important;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3) !important;
    transition: all 0.3s ease !important;
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg, #00F0FF 0%, #7000FF 100%) !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 50px !important;
    padding: 0.5rem 2rem !important;
    font-weight: 600 !important;
    letter-spacing: 1px !important;
    box-shadow: 0 4px 15px rgba(0, 240, 255, 0.4) !important;
    transition: all 0.3s ease !important;
}

.stButton > button:hover {
    transform: scale(1.05) !important;
    box-shadow: 0 6px 20px rgba(112, 0, 255, 0.6) !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: rgba(5, 5, 10, 0.75) !important;
    backdrop-filter: blur(20px) !important;
    border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
}

/* Text Inputs */
.stTextInput > div > div > input, .stTextArea > div > div > textarea, .stSelectbox > div > div > div {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    color: #fff !important;
    border-radius: 10px !important;
}
.stTextInput > div > div > input:focus, .stTextArea > div > div > textarea:focus {
    border-color: #00F0FF !important;
    box-shadow: 0 0 10px rgba(0, 240, 255, 0.2) !important;
}

/* --- OVERRIDING EXISTING CLASSES FOR UI_COMPONENTS --- */
.main-header {
    background: rgba(255, 255, 255, 0.05) !important;
    backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 20px !important;
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3) !important;
}
.main-header h1 {
    background: -webkit-linear-gradient(45deg, #00F0FF, #7000FF) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
}
.template-card, .feature-card, .profile-card {
    background: rgba(255, 255, 255, 0.03) !important;
    backdrop-filter: blur(15px) !important;
    border: 1px solid rgba(255, 255, 255, 0.1) !important;
    border-radius: 20px !important;
}
.template-card:hover, .feature-card:hover, .profile-card:hover {
    transform: translateY(-5px) !important;
    box-shadow: 0 8px 32px 0 rgba(0, 240, 255, 0.2) !important;
    border: 1px solid rgba(0, 240, 255, 0.3) !important;
}
"""

with open('style/style.css', 'w', encoding='utf-8') as f:
    f.write(new_css + '\n' + original_css)
