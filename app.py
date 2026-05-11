import streamlit as st
from dotenv import load_dotenv
import os
import requests

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain_google_genai import ChatGoogleGenerativeAI

# =========================
# LOAD ENV
# =========================

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="SemarTrip AI",
    page_icon="🌆",
    layout="centered"
)

# =========================
# CUSTOM CSS
# =========================

st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #1e293b,
        #334155
    );
    color: white;
}

/* Main Title */
.main-title {
    font-size: 42px;
    font-weight: bold;
    color: white;
    text-align: center;
    margin-top: 10px;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    margin-bottom: 30px;
}

/* User Bubble */
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-user"]) {
    background-color: #2563eb;
    border-radius: 16px;
    padding: 12px;
    margin: 10px 0;
}

/* Assistant Bubble */
[data-testid="stChatMessage"]:has(div[data-testid="chatAvatarIcon-assistant"]) {
    background-color: #1e293b;
    border-radius: 16px;
    padding: 12px;
    margin: 10px 0;
    border: 1px solid #334155;
}

/* Chat Input */
.stChatInputContainer {
    background-color: rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 10px;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #0f172a;
}

/* Sidebar Text */
section[data-testid="stSidebar"] * {
    color: white;
}

/* Button */
.stButton button {
    width: 100%;
    border-radius: 12px;
    background: linear-gradient(
        90deg,
        #2563eb,
        #06b6d4
    );
    color: white;
    border: none;
    padding: 10px;
    font-weight: bold;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {
    background: #475569;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown("""
<div class="main-title">
    🌆 SemarTrip AI
</div>

<div class="subtitle">
    Travel Assistant Kota Semarang Berbasis Gemini AI
</div>
""", unsafe_allow_html=True)

# =========================
# SIDEBAR
# =========================

with st.sidebar:

    st.title("📍 Menu Cepat")

    st.markdown("---")

    st.markdown("### ✨ Rekomendasi")

    if st.button("🏛️ Wisata Populer"):
        st.session_state.quick_prompt = (
            "Rekomendasi wisata populer di Semarang"
        )

    if st.button("🍜 Kuliner Legendaris"):
        st.session_state.quick_prompt = (
            "Kuliner legendaris Semarang"
        )

    if st.button("☕ Cafe Estetik"):
        st.session_state.quick_prompt = (
            "Cafe estetik di Semarang"
        )

    if st.button("🗺️ Itinerary 2 Hari"):
        st.session_state.quick_prompt = (
            "Buat itinerary 2 hari di Semarang"
        )

    if st.button("🌦️ Cuaca Hari Ini"):
        st.session_state.quick_prompt = (
            "Cuaca Semarang hari ini"
        )

    st.markdown("---")

    st.markdown("### ℹ️ Tentang")

    st.write(
        """
        SemarTrip AI membantu wisatawan
        mendapatkan rekomendasi wisata,
        kuliner, itinerary, dan tips
        perjalanan di Kota Semarang.
        """
    )

# =========================
# SESSION STATE
# =========================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        return_messages=True
    )

if "conversation" not in st.session_state:

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0.8,
        google_api_key=GOOGLE_API_KEY
    )

    st.session_state.conversation = ConversationChain(
        llm=llm,
        memory=st.session_state.memory,
        verbose=False
    )

# =========================
# WEATHER FUNCTION
# =========================

def get_weather(city="Semarang"):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"q={city}&appid={WEATHER_API_KEY}"
        f"&units=metric&lang=id"
    )

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        temp = data["main"]["temp"]
        desc = data["weather"][0]["description"]

        return (
            f"Cuaca di {city} saat ini "
            f"{desc} dengan suhu {temp}°C"
        )

    return "Data cuaca tidak tersedia"

# =========================
# SYSTEM PROMPT
# =========================

SYSTEM_PROMPT = """
Kamu adalah SemarTrip AI.

Travel assistant khusus Kota Semarang.

Kepribadian:
- Friendly
- Santai
- Seperti tour guide lokal
- Natural
- Informatif

Tugas:
- Memberikan rekomendasi wisata
- Memberikan rekomendasi kuliner
- Membuat itinerary
- Memberikan tips perjalanan
- Memberikan estimasi budget
- Menjawab pertanyaan wisata Semarang

Gunakan Bahasa Indonesia.

Contoh gaya bicara:
"Kalau kamu suka tempat estetik,
Kota Lama wajib banget masuk list 👌"
"""

# =========================
# DISPLAY CHAT
# =========================

for msg in st.session_state.messages:

    with st.chat_message(
        msg["role"],
        avatar="🧑" if msg["role"] == "user" else "🌆"
    ):
        st.markdown(msg["content"])

# =========================
# QUICK PROMPT
# =========================

if "quick_prompt" in st.session_state:

    prompt = st.session_state.quick_prompt
    del st.session_state.quick_prompt

else:

    prompt = st.chat_input(
        "Tanya seputar wisata Semarang..."
    )

# =========================
# USER INPUT
# =========================

if prompt:

    # User Message
    with st.chat_message("user", avatar="🧑"):
        st.markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Weather Detection
    if "cuaca" in prompt.lower():

        weather_info = get_weather()

        final_prompt = f"""
        {SYSTEM_PROMPT}

        Informasi cuaca realtime:
        {weather_info}

        User:
        {prompt}
        """

    else:

        final_prompt = f"""
        {SYSTEM_PROMPT}

        User:
        {prompt}
        """

    # AI Response
    with st.spinner(
        "🌆 SemarTrip AI sedang menyiapkan rekomendasi..."
    ):

        response = st.session_state.conversation.predict(
            input=final_prompt
        )

    # Assistant Message
    with st.chat_message(
        "assistant",
        avatar="🌆"
    ):

        st.markdown(response)

    # Save Assistant Message
    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

# =========================
# FOOTER
# =========================

st.markdown("""
<hr style="margin-top:30px;border:1px solid #334155">

<div style="
text-align:center;
color:#94a3b8;
padding-bottom:20px;
">

🌆 SemarTrip AI • Powered by Gemini 2.5 Flash

</div>
""", unsafe_allow_html=True)