import streamlit as st
import random

st.set_page_config(
    page_title="Hai, aku Galuh Ayu!",
    page_icon="🌸",
    layout="centered"
)

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg,
            #ffe4f0 0%,
            #fff5d6 35%,
            #e6ffe6 70%,
            #e6f0ff 100%);
        background-size: 300% 300%;
        animation: gradientShift 15s ease infinite;
    }
    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    h1 {
        background: linear-gradient(90deg, #ff9ec4, #ffd66b, #a8e6a8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3rem !important;
        text-align: center;
        animation: float 3s ease-in-out infinite;
        font-weight: 800 !important;
    }
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-12px); }
    }

    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #8a7a6a;
        margin-bottom: 30px;
    }

    .card {
        background: rgba(255, 255, 255, 0.85);
        padding: 25px 30px;
        border-radius: 25px;
        box-shadow: 0 10px 30px rgba(255, 158, 196, 0.25);
        border: 2px solid rgba(255, 214, 107, 0.4);
        margin: 20px 0;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 40px rgba(255, 158, 196, 0.4);
    }

    .card h3 {
        color: #ff69b4;
        margin-top: 0;
    }

    .identitas p {
        font-size: 1.15rem;
        color: #5a4a3a;
        margin: 8px 0;
    }

    .quote-box {
        text-align: center;
        font-style: italic;
        font-size: 1.2rem;
        color: #a86a9a;
        padding: 20px;
        background: rgba(255, 245, 214, 0.6);
        border-radius: 20px;
        border: 2px dashed #ffd66b;
    }

    .footer {
        text-align: center;
        color: #b0a090;
        font-size: 0.9rem;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🌸 Hai, aku Galuh Ayu!")
st.markdown('<p class="subtitle">Kalo ini gambarnya Seonghyeon</p>', unsafe_allow_html=True)

try:
    st.image("sy.jpg", use_container_width=True)
except:
    st.info("Fotonya belum ditambahin")

st.markdown("""
<div class="card identitas">
    <h3>👤 Identitas</h3>
    <p><b>Nama:</b> (Galuh Ayu Cahyaningrum)</p>
    <p><b>NIM:</b> (2615016094)</p>
    <p><b>Prodi:</b> (Sistem Informasi)</p>
</div>
""", unsafe_allow_html=True)

quotes = [
    "katanya coding is fun..",
]

st.markdown("AKU ODGJ (Oasis Dalam Genggaman Jiwa)")
st.video("https://youtu.be/tI-5uv4wryI?si=l28uxr3KvrESkjBk")

st.markdown('<p class="footer">by. galuh (dibantu deepseek muach)</p>', unsafe_allow_html=True)