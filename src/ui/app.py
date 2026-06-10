import streamlit as st

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Mainframe DB2 Knowledge Assistant",
    page_icon="🖥️",
    layout="wide"
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>

.stApp {
    background-color: #0f172a;
    color: white;
}

section[data-testid="stSidebar"] {
    background-color: #111827;
    border-right: 1px solid #1f2937;
}

.main-title {
    font-size: 36px;
    font-weight: bold;
    color: #60a5fa;
    margin-bottom: 10px;
}

.subtitle {
    color: #94a3b8;
    margin-bottom: 30px;
}

.chat-card {
    background-color: #1e293b;
    padding: 20px;
    border-radius: 16px;
    margin-bottom: 20px;
    border: 1px solid #334155;
}

.user-card {
    background-color: #2563eb;
    padding: 15px;
    border-radius: 16px;
    margin-bottom: 15px;
    text-align: right;
}

.source-card {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 14px;
    margin-bottom: 12px;
    border: 1px solid #334155;
}

.metric-card {
    background-color: #111827;
    border-radius: 16px;
    padding: 15px;
    text-align: center;
    border: 1px solid #334155;
}

</style>
""", unsafe_allow_html=True)

# ---------------- Sidebar ----------------
with st.sidebar:
    st.title("🖥️ Mainframe DB2")

    st.markdown("---")

    st.button("➕ New Chat")
    st.button("🕒 Chat History")
    st.button("📂 Saved Queries")
    st.button("📚 Knowledge Base")
    st.button("⚙️ Settings")

    st.markdown("---")

    st.subheader("Knowledge Areas")

    st.write("📌 DB2 Administration")
    st.write("📌 OMEGAMON Alerts")
    st.write("📌 DB2 Utilities")
    st.write("📌 Performance Tuning")
    st.write("📌 Disaster Recovery")
    st.write("📌 Incident RCA")

# ---------------- Main Layout ----------------
col1, col2 = st.columns([3, 1])

# ---------------- Chat Section ----------------
with col1:

    st.markdown(
        '<div class="main-title">Mainframe DB2 Knowledge Assistant</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">AI-powered enterprise assistant for DB2 & Mainframe troubleshooting</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="user-card">
    How to check DB2 buffer pool status?
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="chat-card">

    <h4>🤖 Assistant</h4>

    <b>Method 1: Use DISPLAY BUFFERPOOL</b>

    <br><br>

    <code>
    -DISPLAY BUFFERPOOL(BP0)
    </code>

    <br><br>

    This command displays buffer pool statistics, hit ratio, and current status.

    <br><br>

    <b>Recommended:</b> Monitor using OMEGAMON for real-time metrics.

    </div>
    """, unsafe_allow_html=True)

    st.chat_input("Ask anything about DB2, Mainframe, OMEGAMON...")

# ---------------- Right Panel ----------------
with col2:

    st.subheader("📄 Sources")

    st.markdown("""
    <div class="source-card">
    DB2 Admin Guide <br>
    Page 142
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="source-card">
    OMEGAMON Monitoring SOP
    </div>
    """, unsafe_allow_html=True)

    st.subheader("💡 Suggested Questions")

    st.write("• What causes lock escalation?")
    st.write("• How to improve DB2 performance?")
    st.write("• Explain REORG vs RUNSTATS")

    st.subheader("📊 System Status")

    st.success("LLM Connected")
    st.info("Knowledge Base Ready")