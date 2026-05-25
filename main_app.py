import streamlit as st
import time

def run_subtitle_app():
    # --- 🎨 ស្ទីលលំដាប់ Premium SaaS Dashboard ---
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Khmer+OS+Muol+Light&family=Kantumruy+Pro:wght@300;400;500;700&display=swap');
    
    /* 1. កំណត់ Font ឱ្យមានតុល្យភាព */
    html, body, [class*="css"], [class*="st-"], p, span, div, label, li, button, input, select, textarea {
        font-family: 'Kantumruy Pro', sans-serif !important;
    }

    /* 2. កំណត់ផ្ទៃខាងក្រោយបែប Deep Slate Dark Mode */
    .stApp {
        background-color: #0F172A !important;
    }

    /* 3. កំណត់របារចំហៀង Sidebar ឱ្យកាន់តែរលោង និងប្រណីត */
    section[data-testid="stSidebar"] {
        background-color: #0B0F19 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    /* 4. ចំណងជើងកម្មវិធីបែបលំដាប់ខ្ពស់ (Premium Typography) */
    .main-title {
        text-align: center;
        font-family: 'Khmer OS Muol Light', sans-serif !important;
        background: linear-gradient(135deg, #F8FAFC 0%, #94A3B8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 34px;
        font-weight: bold;
        margin-bottom: 5px;
        letter-spacing: 0.5px;
    }
    .sub-title {
        text-align: center;
        font-size: 15px;
        color: #94A3B8 !important;
        margin-bottom: 35px;
    }

    /* 5. កែច្នៃប្រអប់ Container ឱ្យដូចជាកញ្ចក់ខ្មៅរលោង (Black Obsidian Glass) */
    div[data-testid="stForm"], 
    .stFileUploader, 
    div[data-testid="stNotification"],
    div.stAlert {
        background-color: rgba(30, 41, 59, 0.5) !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25) !important;
        padding: 24px !important;
    }

    /* 6. កែច្នៃប៊ូតុងក្នុង Sidebar (Menu Navigation) */
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] label {
        background-color: rgba(30, 41, 59, 0.4) !important;
        color: #94A3B8 !important;
        border: 1px solid rgba(255, 255, 255, 0.05) !important;
        border-radius: 10px !important;
        padding: 12px 16px !important;
        cursor: pointer;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
        width: 100%;
        margin-bottom: 4px;
    }
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
        background-color: rgba(30, 41, 59, 0.8) !important;
        color: #F8FAFC !important;
        transform: translateX(2px);
    }
    /* ម៉ឺនុយដែលបានជ្រើសរើស (Gradient active state) */
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
        background: linear-gradient(135deg, #6366F1 0%, #3B82F6 100%) !important;
        border-color: rgba(99, 102, 241, 0.5) !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.2) !important;
    }
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] span {
        color: #FFFFFF !important;
        font-weight: 600 !important;
    }
    /* លាក់សញ្ញារង្វង់មូលដើម */
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] [data-testid="stHighlightContainer"] {
        display: none !important;
    }
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] label div:first-child {
        display: none !important;
    }

    /* 7. កែច្នៃប៊ូតុងចម្បងឱ្យមានលក្ខណៈ Premium Gradient */
    div.stButton > button:first-child {
        width: 100%;
        background: linear-gradient(135deg, #6366F1 0%, #3B82F6 100%) !important;
        color: #FFFFFF !important;
        font-family: 'Kantumruy Pro', sans-serif !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
        padding: 14px 0px !important;
        font-size: 16px !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        border: none !important;
        box-shadow: 0 4px 20px rgba(99, 102, 241, 0.3) !important;
    }
    div.stButton > button:first-child:hover {
        background: linear-gradient(135deg, #4F46E5 0%, #2563EB 100%) !important;
        box-shadow: 0 6px 24px rgba(99, 102, 241, 0.45) !important;
        transform: translateY(-1px);
    }

    /* ប៊ូតុង Logout */
    div[data-testid="stSidebar"] button {
        background-color: rgba(239, 68, 68, 0.1) !important;
        color: #F87171 !important;
        border: 1px solid rgba(239, 68, 68, 0.2) !important;
        border-radius: 8px !important;
        font-weight: 500 !important;
    }
    div[data-testid="stSidebar"] button:hover {
        background-color: rgba(239, 68, 68, 0.2) !important;
        color: #EF4444 !important;
    }

    /* កែសម្រួលអត្ថបទ និងពណ៌ Selectbox, Text Area */
    div[data-baseweb="select"] {
        background-color: #1E293B !important;
        border-radius: 8px !important;
    }
    textarea {
        background-color: #0F172A !important;
        color: #F8FAFC !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
    }
    label {
        color: #E2E8F0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # ==========================================
    # របារចំហៀង (Sidebar)
    # ==========================================
    with st.sidebar:
        st.markdown("<h3 style='color: #F8FAFC !important;'>🟢 គណនីរបស់អ្នក</h3>", unsafe_allow_html=True)
        st.success("ស្ថានភាព៖ កំពុងប្រើប្រាស់")
        
        st.write("") 
        
        st.markdown("<h4 style='color: #94A3B8 !important;'>🗺️ ម៉ឺនុយបញ្ជា</h4>", unsafe_allow_html=True)
        menu_option = st.radio(
            "សូមជ្រើសរើសផ្ទាំង៖",
            ["🎙️ បកប្រែសំឡេងទៅជាអក្សរ", "⚙️ ការកំណត់"],
            label_visibility="collapsed"
        )
        
        st.write("") 
        if st.button("ចាកចេញពីប្រព័ន្ធ (Logout)", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

    # ==========================================
    # ផ្ទាំងកណ្តាល (Main Workflow Logic)
    # ==========================================
    
    # ------------------------------------------
    # លក្ខខណ្ឌទី ១៖ ផ្ទាំង "🎙️ បកប្រែសំឡេងទៅជាអក្សរ"
    # ------------------------------------------
    if menu_option == "🎙️ បកប្រែសំឡេងទៅជាអក្សរ":
        st.markdown('<div class="main-title">ប្រព័ន្ធបកប្រែ Subtitle & សំឡេង</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-title">បម្លែងឯកសារសំឡេង ឬ Subtitle ទៅជាភាសាខ្មែរដោយស្វ័យប្រវត្តិជាមួយ AI</div>', unsafe_allow_html=True)

        # --- ផ្នែកទី ១៖ បញ្ចូលឯកសារ ---
        st.markdown("<h4 style='color: #F8FAFC;'>📂 ជំហានទី ១៖ បញ្ចូលឯកសារ</h4>", unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "សូមទាញឯកសារទម្លាក់ទីនេះ (គាំទ្រ៖ MP3, WAV, M4A, SRT)", 
            type=['mp3', 'wav', 'm4a', 'srt']
        )
        
        file_type = None
        if uploaded_file:
            file_type = uploaded_file.name.split('.')[-1].lower()
            st.success(f"✅ ឯកសារទទួលបានជោគជ័យ៖ {uploaded_file.name}")

        st.divider()

        # --- ផ្នែកទី ២៖ កំណត់ម៉ូដែល AI ---
        st.markdown("<h4 style='color: #F8FAFC;'>🤖 ជំហានទី ២៖ ជ្រើសរើសម៉ូដែល AI</h4>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        
        with col1:
            if file_type == 'srt':
                st.info("ℹ️ ឯកសារជាអត្ថបទ (SRT) មិនត្រូវការម៉ូដែលស្ដាប់សំឡេងឡើយ។")
                transcribe_model = "មិនត្រូវការ"
            else:
                transcribe_model = st.selectbox(
                    "👂 ម៉ូដែលសម្រាប់ស្តាប់សំឡេង", 
                    ["Whisper-1 (OpenAI - ច្បាស់បំផុត)", "Whisper-Large-v3"]
                )
                
        with col2:
            translate_model = st.selectbox(
                "📝 ម៉ូដែលសម្រាប់បកប្រែជាខ្មែរ", 
                ["Gemini 1.5 Pro (Google - ឆ្លាតបំផុត)", "Gemini 1.5 Flash (Google)", "GPT-4o (OpenAI)"]
            )

        st.divider()

        # --- ផ្នែកទី ៣៖ ប៊ូតុងបញ្ជា (Action) ---
        st.markdown("<h4 style='color: #F8FAFC;'>🚀 ជំហានទី ៣៖ ចាប់ផ្ដើមប្រតិបត្តិការ</h4>", unsafe_allow_html=True)
        
        if 'processing_done' not in st.session_state:
            st.session_state.processing_done = False

        if st.button("ដំណើរការបម្លែងឯកសារឥឡូវនេះ", type="primary", use_container_width=True):
            if not uploaded_file:
                st.warning("⚠️ សូមបញ្ចូលឯកសារនៅ [ជំហានទី ១] សិន មុននឹងបន្ត!")
            else:
                st.info(f"🔄 កំពុងដំណើរការឯកសារ {uploaded_file.name}... សូមរង់ចាំបន្តិច!")
                
                progress_bar = st.progress(0)
                with st.spinner("ប្រព័ន្ធ AI កំពុងដំណើរការ..."):
                    for i in range(1, 101, 20):
                        time.sleep(0.4)
                        progress_bar.progress(i)
                    
                st.success("🎉 ដំណើរការបកប្រែជោគជ័យ!")
                st.session_state.processing_done = True
                
        # --- ផ្នែកទី ៤៖ បង្ហាញលទ្ធផល និងទាញយក ---
        if st.session_state.processing_done and uploaded_file:
            st.divider()
            st.markdown("<h4 style='color: #F8FAFC;'>📄 លទ្ធផលទទួលបានពី AI (គំរូ)</h4>", unsafe_allow_html=True)
            
            sample_translated_text = (
                "1\n00:00:01,000 --> 00:00:04,000\nសួស្តីអ្នកទាំងអស់គ្នា! សូមស្វាគមន៍មកកាន់ការទស្សនា។\n\n"
                "2\n00:00:04,500 --> 00:00:08,000\nថ្ងៃនេះយើងនឹងជជែកគ្នាអំពីបច្ចេកវិទ្យាបញ្ញាសិប្បនិម្មិត AI។"
            )
            
            st.text_area("អត្ថបទ Subtitle ជាភាសាខ្មែរ៖", value=sample_translated_text, height=150)
            
            st.download_button(
                label="📥 ទាញយកឯកសារបកប្រែរួច (.srt)",
                data=sample_translated_text,
                file_name=f"translated_{uploaded_file.name.split('.')[0]}.srt",
                mime="text/plain",
                use_container_width=True
            )

    # ------------------------------------------
    # លក្ខខណ្ឌទី ២៖ ផ្ទាំង "⚙️ ការកំណត់"
    # ------------------------------------------
    elif menu_option == "⚙️ ការកំណត់":
        st.markdown('<div class="main-title">ការកំណត់ប្រព័ន្ធ</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-title">គ្រប់គ្រងគណនី និងការកំណត់ API សម្រាប់ការបកប្រែ</div>', unsafe_allow_html=True)
        
        with st.container():
            st.markdown("<h4 style='color: #F8FAFC;'>⚙️ កម្រងព័ត៌មាន និង API Keys</h4>", unsafe_allow_html=True)
            
            with st.form("settings_form"):
                st.text_input("🔑 Google Gemini API Key:", type="password", placeholder="បញ្ចូល API Key របស់ Gemini នៅទីនេះ")
                st.text_input("🔑 OpenAI API Key:", type="password", placeholder="បញ្ចូល API Key របស់ OpenAI នៅទីនេះ")
                
                st.divider()
                st.markdown("<h5 style='color: #E2E8F0;'>⚙️ ការកំណត់ទូទៅ</h5>", unsafe_allow_html=True)
                st.selectbox("ជ្រើសរើសភាសាចំណុចប្រទាក់ (Interface Language)", ["ភាសាខ្មែរ", "English"])
                st.checkbox("ចងចាំការកំណត់នៅលើកម្មវិធីនេះ", value=True)
                
                save_btn = st.form_submit_button("រក្សាទុកការកំណត់")
                if save_btn:
                    st.toast("💾 រក្សាទុកការកំណត់បានជោគជ័យ!", icon="✅")

# ហៅមកប្រើប្រាស់
if __name__ == "__main__":
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = True
        
    if st.session_state.logged_in:
        run_subtitle_app()
