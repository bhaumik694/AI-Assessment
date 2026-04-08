import streamlit as st
import requests

# ---- PAGE CONFIG ----
st.set_page_config(page_title="AI Learning Agent", layout="wide")

# ---- CUSTOM CSS ----
st.markdown("""
<style>
.main {
    padding: 2rem;
}

/* Header */
.title {
    font-size: 2.2rem;
    font-weight: 700;
    color: #ffffff;
}
.subtitle {
    font-size: 1.1rem;
    color: #cccccc;
}

/* Card */
.card {
    padding: 1.5rem;
    border-radius: 12px;
    background-color: #1e1e1e;
    margin-bottom: 1rem;
    color: #ffffff;
}

/* MCQ Box */
.mcq-box {
    padding: 1rem;
    border-radius: 10px;
    background-color: #262730;
    margin-bottom: 12px;
    color: #ffffff;
    border: 1px solid #333;
}

/* Answer */
.answer {
    color: #00ffae;
    font-weight: bold;
}

/* Improve spacing */
.block-container {
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown('<div class="title">🤖 AI Learning Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Generate, Review & Refine Educational Content</div>', unsafe_allow_html=True)

st.divider()

# ---- INPUT SECTION ----
col1, col2, col3 = st.columns([1,2,1])

with col2:
    grade = st.selectbox("🎓 Select Grade", list(range(1, 11)), index=3)
    topic = st.text_input("📘 Topic", placeholder="e.g. Fractions, Photosynthesis")

    generate = st.button("🚀 Generate Content", use_container_width=True)

# ---- GENERATE ----
if generate:

    if not topic:
        st.warning("⚠️ Please enter a topic")
        st.stop()

    with st.spinner("⚡ AI Agents Working..."):

        try:
            response = requests.post(
                "http://127.0.0.1:8000/generate",
                json={"grade": grade, "topic": topic},
                timeout=60
            )
        except Exception as e:
            st.error("❌ Backend not reachable")
            st.text(str(e))
            st.stop()

        if response.status_code != 200:
            st.error("❌ Backend Error")
            st.text(response.text)
            st.stop()

        try:
            data = response.json()
        except:
            st.error("❌ Invalid response from backend")
            st.text(response.text)
            st.stop()

    st.divider()

    # =========================
    # 📘 GENERATOR OUTPUT
    # =========================
    st.markdown("## 📘 Generated Content")

    st.markdown(f"""
    <div class="card">
        {data['initial_output']['explanation']}
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📝 Quiz")

    for i, mcq in enumerate(data["initial_output"]["mcqs"], 1):
        st.markdown(f"""
        <div class="mcq-box">
            <b>Q{i}. {mcq['question']}</b><br><br>
            {'<br>'.join([f"• {opt}" for opt in mcq['options']])}
            <br><br>
            <span class="answer">✔ Answer: {mcq['answer']}</span>
        </div>
        """, unsafe_allow_html=True)

    # =========================
    # 🧠 REVIEWER
    # =========================
    st.divider()
    st.markdown("## 🧠 AI Review")

    status = data["review"]["status"]

    if status == "pass":
        st.success("✅ Content Approved")
    else:
        st.error("❌ Needs Improvement")

    for fb in data["review"]["feedback"]:
        st.write(f"• {fb}")

    # =========================
    # 🔁 REFINED OUTPUT
    # =========================
    if data["refined_output"]:
        st.divider()
        st.markdown("## 🔁 Improved Content")

        st.markdown(f"""
        <div class="card">
            {data['refined_output']['explanation']}
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### 📝 Updated Quiz")

        for i, mcq in enumerate(data["refined_output"]["mcqs"], 1):
            st.markdown(f"""
            <div class="mcq-box">
                <b>Q{i}. {mcq['question']}</b><br><br>
                {'<br>'.join([f"• {opt}" for opt in mcq['options']])}
                <br><br>
                <span class="answer">✔ Answer: {mcq['answer']}</span>
            </div>
            """, unsafe_allow_html=True)