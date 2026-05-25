import streamlit as st

def run_subtitle_app():
    # --- 🎨 កំណត់ Font អក្សរខ្មែរឱ្យស្អាតគ្រប់ជ្រុងទាំងអស់ ---
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Khmer+OS+Muol+Light&family=Kantumruy+Pro&display=swap');
    
    /* កំណត់អក្សរទូទៅទាំងអស់ឱ្យប្រើ Kantumruy Pro ឱ្យស្អាតស្មើគ្នា */
    html, body, [class*="css"], [class*="st-"], p, span, div, label, li, button, input, select, textarea {
        font-family: 'Kantumruy Pro', sans-serif !important;
    }

    /* កំណត់ចំណងជើង (Heading) ទាំងអស់ឱ្យប្រើ Khmer OS Muol Light និងពណ៌ខៀវ */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Khmer OS Muol Light', sans-serif !important;
        color: #1a73e8 !important;
    }
    
    /* ចំណងជើងកណ្តាល */
    .main-title {
        text-align: center;
        font-family: 'Khmer OS Muol Light', sans-serif !important;
        color: #1a73e8 !important;
        font-size: 32px;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        font-family: 'Kantumruy Pro', sans-serif !important;
        font-size: 16px;
        color: #5F6368 !important;
        margin-bottom: 30px;
    }
    
    /* រចនាប៊ូតុងដំណើរការឱ្យធំ លេចធ្លោ និងអក្សរស្អាត */
    div.stButton > button:first-child {
        width: 100%;
        background-color: #1a73e8 !important;
        color: white !important;
        font-family: 'Kantumruy Pro', sans-serif !important;
        font-weight: bold !important;
        border-radius: 8px !important;
        padding: 12px 0px !important;
        font-size: 16px !important;
        transition: 0.3s;
        border: none !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #1557b0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # ==========================================
    # របារចំហៀង (Sidebar) - លុប API Keys ចេញ ទុកតែ Logout
    # ==========================================
    with st.sidebar:
        st.markdown("### 🟢 គណនីរបស់អ្នក")
        st.success("ស្ថានភាព៖ កំពុងប្រើប្រាស់")
        if st.button("ចាកចេញពីប្រព័ន្ធ (Logout)", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

    # ==========================================
    # ផ្ទាំងកណ្តាល (Main Workflow)
    # ==========================================
    st.markdown('<div class="main-title">ប្រព័ន្ធបកប្រែ Subtitle & សំឡេង</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">បម្លែងឯកសារសំឡេង ឬ Subtitle ទៅជាភាសាខ្មែរដោយស្វ័យប្រវត្តិជាមួយ AI</div>', unsafe_allow_html=True)

    # --- ផ្នែកទី ១៖ បញ្ចូលឯកសារ ---
    st.markdown("#### 📂 ជំហានទី ១៖ បញ្ចូលឯកសារ")
    with st.container():
        uploaded_file = st.file_uploader("សូមទាញឯកសារទម្លាក់ទីនេះ (គាំទ្រ៖ MP3, WAV, M4A, SRT)", type=['mp3', 'wav', 'm4a', 'srt'])
        if uploaded_file:
            st.success(f"✅ ឯកសារទទួលបានជោគជ័យ៖ {uploaded_file.name}")

    st.divider()

    # --- ផ្នែកទី ២៖ កំណត់ម៉ូដែល AI ---
    st.markdown("#### 🤖 ជំហានទី ២៖ ជ្រើសរើសម៉ូដែល AI")
    col1, col2 = st.columns(2)
    with col1:
        transcribe_model = st.selectbox("👂 ម៉ូដែលសម្រាប់ស្តាប់សំឡេង", ["Whisper-1 (OpenAI - ច្បាស់បំផុត)"])
    with col2:
        translate_model = st.selectbox("📝 ម៉ូដែលសម្រាប់បកប្រែជាខ្មែរ", ["Gemini 1.5 Pro (Google - ឆ្លាតបំផុត)", "Gemini 1.5 Flash (Google)", "GPT-4o (OpenAI)"])

    st.divider()

    # --- ផ្នែកទី ៣៖ ប៊ូតុងបញ្ជា (Action) ---
    st.markdown("#### 🚀 ជំហានទី ៣៖ ចាប់ផ្ដើមប្រតិបត្តិការ")
    
    # ប៊ូតុងដំណើរការ
    if st.button("ដំណើរការបម្លែងឯកសារឥឡូវនេះ", type="primary", use_container_width=True):
        if not uploaded_file:
            st.warning("⚠️ សូមបញ្ចូលឯកសារនៅ [ជំហានទី ១] សិន មុននឹងបន្ត!")
        else:
            st.info(f"🔄 កំពុងដំណើរការឯកសារ {uploaded_file.name}... សូមរង់ចាំបន្តិច!")
            with st.spinner("ប្រព័ន្ធ AI កំពុងធ្វើការបកប្រែ..."):
                import time
                time.sleep(2) # ធ្វើពុតជាកំពុងដំណើរការសិន
                st.success("🎉 ដំណើរការបកប្រែជោគជ័យ! (ត្រៀមចូលវគ្គកូដ AI ពិតប្រាកដ)")
