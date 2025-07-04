# 🚀 LinkedIn Post Generator using GroqAI & Streamlit

A lightweight and beginner-friendly Streamlit app that helps you generate LinkedIn-style posts inspired by creators like **Love Babbar** — using Groq’s blazing-fast LLaMA 3.2 API. 🧠⚡

This project is a part of my learning journey, where I’m exploring prompt engineering, Streamlit apps, and large language models.

![Workflow](architexture.jpg)

---

## 🧩 How It Works

The app runs in **two major stages**:

### ✅ Stage 1 — Post Preprocessing
- Raw LinkedIn posts are **manually collected** (for now) from creators.
- These posts are enriched using **Groq LLaMA 3.2** to extract:
  - **Topic**
  - **Tone / Language**
  - **Length**

### ✅ Stage 2 — Post Generation
- User selects `Topic`, `Language`, and `Length`.
- A **custom prompt** is generated.
- Groq LLaMA 3.2 model then generates a LinkedIn-style post based on the selected preferences.

---

## ⚙️ Tech Stack

- **Frontend**: Streamlit
- **LLM Provider**: [Groq](https://groq.com) API with `llama3-70b-verse`
- **Environment**: Python 3.13, dotenv
- **Prompt Framework**: LangChain

---

## 🔧 Setup Instructions

1. **Clone the Repo**
   ```bash
   git clone https://github.com/AryanRajTalekar/LinkedIn-Post-Generator-Using-Groqai.git
   cd LinkedIn-Post-Generator-Using-Groqai
2.Install Requirements
  pip install -r requirements.txt
3.Set Up Environment
  Create a .env file:GROQ_API_KEY=your_actual_groq_api_key_here
4.Run the App
  streamlit run main.py

🚧 Future Improvements
🔄 Auto-scraping LinkedIn posts via LinkedIn API / scraping tools

🗃️ Add MongoDB for storing enriched prompts

🌍 Add multi-language support

🧪 Improve prompt templates using real-world feedback


🙌 Acknowledgements
Big thanks to:

Groq for ultra-fast inference with LLaMA models

Love Babbar — inspiration for post styles

Streamlit for the clean and intuitive UI framework
