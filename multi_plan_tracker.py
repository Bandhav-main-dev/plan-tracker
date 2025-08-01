import streamlit as st
import json
import os
from datetime import datetime
import google.generativeai as genai

# === CONFIG ===
DATA_FILES = {
    "🇯🇵 Japan AI Engineer Plan": "japan_ai_plan.json",
    "🗽 Manhattan AI Engineer Plan": "manhattan_ai_plan.json"
}
CHAT_LOG_FILE = "chat_log.json"
GOOGLE_API_KEY = "AIzaSyCCApuSm68ur-QNfp62g4UuFnm1cBURb3c"  # You can hardcode if needed

# === INIT Gemini ===
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel("gemini-2.0-flash")
else:
    model = None

# === HELPERS ===
def load_data(path):
    with open(path, "r") as f:
        return json.load(f)

def save_data(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def load_chat_log():
    if not os.path.exists(CHAT_LOG_FILE):
        return []
    with open(CHAT_LOG_FILE, "r") as f:
        return json.load(f)

def save_chat_log(log):
    with open(CHAT_LOG_FILE, "w") as f:
        json.dump(log, f, indent=2)

def generate_chat_response(user_input):
    if model:
        try:
            response = model.generate_content(user_input)
            return response.text.strip()
        except Exception as e:
            return f"Sorry, I couldn't process that. (Error: {e})"
    else:
        return "(Gemini API key not set. Using fallback response.) You're doing great, Bandhav. Keep going! 🔥"

# === PAGE CONFIG ===
st.set_page_config(page_title="Multi AI Dream Tracker", layout="wide")

# === MAIN NAVIGATION ===
main_page = st.sidebar.radio("🧭 Main Menu", ["🏠 Home", "📋 Plan Tracker", "💬 Personal Chat"])

if main_page == "🏠 Home":
    st.title("🌟 Welcome to the AI Engineer Dream Tracker")
    st.markdown("""
    ### 👋 Hello Bandhav!
    This tool helps you stay on track with your dream of becoming a ₹1.2 Cr/year AI Engineer — whether in 🇯🇵 Japan or 🗽 Manhattan.

    - Select a plan from the sidebar
    - Track your monthly progress
    - Save your task completions
    - Build projects that matter

    ---
    📅 Both 12-month roadmaps are powered by Streamlit, JSON, and your ambition. Let's begin your transformation! 💪🔥
    """)

elif main_page == "📋 Plan Tracker":
    st.title("🚀 AI Engineer Plan Tracker")

    # === PLAN SELECT ===
    plan_choice = st.sidebar.selectbox("Select Your Plan", list(DATA_FILES.keys()))
    file_path = DATA_FILES[plan_choice]

    # === LOAD DATA ===
    data = load_data(file_path)
    plan_name = list(data.keys())[0]
    plan = data[plan_name]

    # === NAVIGATION ===
    phase = st.sidebar.radio("🔽 Navigation", list(plan.keys()))

    # === DISPLAY ===
    total = 0
    completed = 0

    if phase in plan:
        st.header(f"{plan_choice} - {phase}")
        for topic, tasks in plan[phase].items():
            st.markdown(f"### 📌 {topic}")
            for i, (task, done) in enumerate(tasks.items()):
                key = f"{plan_choice}-{phase}-{topic}-{i}"
                checked = st.checkbox(task, value=done, key=key)
                plan[phase][topic][task] = checked
                total += 1
                if checked:
                    completed += 1

    # === PROGRESS ===
    progress = completed / total if total > 0 else 0
    st.progress(progress)
    st.info(f"Progress: {completed} / {total} tasks completed")

    # === SAVE ===
    if st.button("💾 Save Progress"):
        save_data(file_path, data)
        st.success("Progress Saved!")

elif main_page == "💬 Personal Chat":
    st.title("💬 Personal AI Chatbot")
    chat_log = load_chat_log()

    for entry in chat_log:
        st.markdown(f"**You:** {entry['user']}")
        st.markdown(f"**Bot:** {entry['bot']}")
        st.markdown("---")

    user_input = st.text_input("Talk to your tracker 👇")
    if st.button("Send") and user_input.strip():
        response = generate_chat_response(user_input)
        st.write(response)
        chat_log.append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "user": user_input,
            "bot": response
        })
        save_chat_log(chat_log)
        st.rerun()
