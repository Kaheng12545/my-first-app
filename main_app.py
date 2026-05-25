import streamlit as st

def run_subtitle_app():
    # --- កំណត់ Font អក្សរខ្មែរឱ្យស្អាត ---
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Khmer+OS+Muol+Light&family=Kantumruy+Pro&display=swap');
    
    .main-title {
        text-align: center;
        color: #1a73e8;
        font-family: 'Khmer OS Muol Light', sans-serif !important;
        font-size: 32px;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        color: #5F6368;
        font-family: 'Kantumruy Pro', sans-serif !important;
        font-size: 16px;
        margin-bottom: 30px;
    }
    </style>
    """, unsafe_allow_html=True)

    # --- ប្រព័ន្ធចងចាំ API Key ---
    if "openai_key" not in st.session_state:
        st.session_state.openai_key = ""
    if "gemini_key" not in st.session_state:
        st.session_state.gemini_key = ""

    # ==========================================
    # របារចំហៀង (Sidebar) - កន្លែងកំណត់សុវត្ថិភាព
    # ==========================================
    with st.sidebar:
        st.markdown("### ⚙️ ការកំណត់ប្រព័ន្ធ (Settings)")
        st.info("🔑 API Keys សម្រាប់ឱ្យ AI ដំណើរការ")
        
        st.session_state.openai_key = st.text_input("1️⃣ OpenAI API Key (ស្តាប់សំឡេង)", value=st.session_state.openai_key, type="password")
        st.session_state.gemini_key = st.text_input("2️⃣ Gemini API Key (បកប្រែ)", value=st.session_state.gemini_key, type="password")
        
        st.divider() # គូសបន្ទាត់
        st.markdown("### 🟢 គណនីរបស់អ្នក")
        st.success("ស្ថានភាព៖ កំពុងប្រើប្រាស់")
        if st.button("ចាកចេញពីប្រព័ន្ធ (Logout)", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

    # ==========================================
    # ផ្ទាំងកណ្តាល (Main Workflow) - តួកម្មវិធី
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
    
    # ប្រើ type="primary" ដើម្បីឱ្យវាចេញពណ៌លេចធ្លោស្អាតតាមស្តង់ដារប្រព័ន្ធ
    if st.button("ដំណើរការបម្លែងឯកសារឥឡូវនេះ", type="primary", use_container_width=True):
        if not uploaded_file:
            st.warning("⚠️ សូមបញ្ចូលឯកសារនៅ [ជំហានទី ១] សិន មុននឹងបន្ត!")
        elif not st.session_state.openai_key or not st.session_state.gemini_key:
            st.error("⚠️ សូមបញ្ចូល API Keys ទាំង ២ នៅរបារខាងឆ្វេងដៃសិន!")
        else:
            st.info(f"🔄 កំពុងដំណើរការឯកសារ {uploaded_file.name}... សូមរង់ចាំបន្តិច!")
            with st.spinner("ប្រព័ន្ធ AI កំពុងធ្វើការបកប្រែ..."):
                import time
                time.sleep(2) # ធ្វើពុតជាកំពុងដំណើរការ
                st.success("🎉 ដំណើរការបកប្រែជោគជ័យ! (ត្រៀមចូលវគ្គកូដ AI ពិតប្រាកដ)")
