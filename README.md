# SemarTrip AI 🌆

AI Chatbot Travel Assistant Kota Semarang berbasis Streamlit + LangChain + Gemini AI.

SemarTrip AI membantu pengguna mendapatkan rekomendasi wisata, kuliner, itinerary, hingga informasi perjalanan di Kota Semarang menggunakan teknologi AI dan Natural Language Processing (NLP).

---

# ✨ Features

- 🤖 AI Chatbot berbasis Gemini 2.5 Flash
- 🌆 Travel Assistant khusus Kota Semarang
- 🧠 Memory Conversation menggunakan LangChain
- 🌦️ Integrasi API Cuaca Realtime
- 🎨 Modern UI dengan Streamlit
- 💬 Chat interface interaktif
- 📍 Quick recommendation menu
- 🗺️ Itinerary generator
- 🍜 Rekomendasi kuliner
- ☕ Cafe & wisata estetik
- 🌐 Bisa diakses publik menggunakan Ngrok

---

# 🛠️ Tech Stack

| Technology | Description |
|---|---|
| Python | Bahasa pemrograman utama |
| Streamlit | Frontend chatbot |
| LangChain | AI orchestration & memory |
| Gemini 2.5 Flash | Large Language Model |
| OpenWeather API | Data cuaca realtime |
| Ngrok | Public deployment |

---

# 📂 Project Structure

```bash
semartrip-ai/
│
├── app.py
├── requirements.txt
├── .env
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone https://github.com/username/semartrip-ai.git
```

## 2. Masuk ke Folder Project

```bash
cd semartrip-ai
```

---

# 🐍 Create Virtual Environment

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 📄 requirements.txt

```txt
streamlit
langchain==0.1.20
langchain-core==0.1.52
langchain-google-genai==1.0.3
google-generativeai
python-dotenv
requests
```

---

# 🔑 API KEY Setup

Buat file `.env`

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
WEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY
```

---

# 🔗 Get API Key

## Gemini API Key

https://aistudio.google.com/app/apikey

## OpenWeather API Key

https://openweathermap.org/api

---

# ▶️ Run Application

```bash
streamlit run app.py
```

Aplikasi akan berjalan di:

```bash
http://localhost:8501
```

---

# 🌐 Run with Ngrok

## Install Ngrok

https://ngrok.com/

## Login Ngrok

```bash
ngrok config add-authtoken YOUR_NGROK_TOKEN
```

## Jalankan Tunnel

```bash
ngrok http 8501
```

Contoh output:

```bash
https://abcd1234.ngrok-free.app
```

Link tersebut dapat diakses publik.

---

# 💡 Example Prompt

## Wisata

```text
Rekomendasi wisata estetik di Semarang
```

## Kuliner

```text
Makanan khas Semarang yang wajib dicoba
```

## Itinerary

```text
Buat itinerary 2 hari 1 malam di Semarang budget mahasiswa
```

## Cuaca

```text
Cuaca Semarang hari ini bagaimana?
```

---

# 🧠 AI Configuration

| Parameter | Value |
|---|---|
| Model | Gemini 2.5 Flash |
| Temperature | 0.8 |
| Language | Bahasa Indonesia |
| Personality | Friendly Local Guide |
| Memory | ConversationBufferMemory |
| Framework | LangChain |

---

# 🎨 UI Features

- Modern Dark Mode
- Glassmorphism Style
- Interactive Sidebar
- Chat Bubble UI
- Loading Spinner
- AI Avatar
- Responsive Layout

---

# 🚀 Future Improvements

- 📍 Google Maps Integration
- 🖼️ Wisata Image Recommendation
- 🎙️ Voice Assistant
- 📄 Export Itinerary to PDF
- 🏨 Hotel Recommendation API
- 💾 Database Chat History
- 🌍 Multi-language Support

---

# 📸 Preview

Tambahkan screenshot aplikasi di sini.

```bash
assets/
└── preview.png
```

Lalu tampilkan:

```markdown
![Preview](assets/preview.png)
```

---

# 📚 Learning Concepts

Project ini mengimplementasikan:

- Natural Language Processing (NLP)
- Large Language Model (LLM)
- Prompt Engineering
- AI Memory
- Streamlit Web App
- REST API Integration
- Conversational AI

---

# 👨‍💻 Author

Nama: Your Name

Project: SemarTrip AI

---

# ⭐ Support

Jika project ini membantu, jangan lupa kasih ⭐ di repository GitHub 😊
