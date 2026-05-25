import streamlit as st
import time

def run_subtitle_app():
    # --- 🎨 កូដ CSS សម្រាប់កែច្នៃកម្មវិធី និងប្រអប់ឯកសារ (Premium Glass File Uploader) ---
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Khmer+OS+Muol+Light&family=Kantumruy+Pro:wght@300;400;500;700&display=swap');
    
    /* កំណត់ Font ទូទៅ */
    html, body, [class*="css"], [class*="st-"], p, span, div, label, li, button, input, select, textarea {
        font-family: 'Kantumruy Pro', sans-serif !important;
    }

    /* ផ្ទៃខាងក្រោយបែប Deep Slate Dark Mode */
    .stApp {
        background-color: #0F172A !important;
    }

    /* របារចំហៀង Sidebar ឱ្យកាន់តែរលោង */
    section[data-testid="stSidebar"] {
        background-color: #0B0F19 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    /* ចំណងជើងកម្មវិធី (Premium Typography) */
    .main-title {
        text-align: center;
        font-family: 'Khmer OS Muol Light', sans-serif !important;
        background: linear-gradient(135deg, #F8FAFC 0%, #94A3B8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        font-size: 15px;
        color: #94A3B8 !important;
        margin-bottom: 35px;
    }

    /* ប្រអប់ Container បែបកញ្ចក់ខ្មៅរលោង */
    div[data-testid="stForm"], 
    div[data-testid="stNotification"],
    div.stAlert {
        background-color: rgba(30, 41, 59, 0.5) !important;
        border-radius: 14px !important;
        border: 1px solid rgba(255, 255, 255, 0.08) !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25) !important;
        padding: 24px !important;
    }

    /* ---------------------------------------------------------------- */
    /* 🛠️ កូដកែច្នៃប្រអប់ File Uploader ឱ្យទៅជាចតុកោណកែងពណ៌សថ្លាកណ្ដាល ស្អាត Premium */
    /* ---------------------------------------------------------------- */
    .stFileUploader {
        background-color: transparent !important;
        border: none !important;
        padding: 0px !important;
    }
    
    /* កែច្នៃប្រអប់ Dropzone (ប្រអប់អូសទម្លាក់) */
    div[data-testid="stFileUploaderDropzone"] {
        background-color: rgba(255, 255, 255, 0.85) !important; /* ពណ៌សថ្លាបែបកញ្ចក់ */
        border: 2px dashed #6366F1 !important; /* គែមឆ្នូតៗពណ៌ស្វាយ */
        border-radius: 16px !important;
        min-height: 200px !important; /* បង្កើនកម្ពស់ឱ្យទៅជាចតុកោណកែងធំ */
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important; /* តម្រឹមទៅកណ្តាល */
        justify-content: center !important; /* តម្រឹមទៅកណ្តាល */
        text-align: center !important;
        transition: all 0.3s ease-in-out !important;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1) !important;
    }
    
    /* ពេលអូសឯកសារមកលើ ឱ្យដូរពណ៌ស្អាត */
    div[data-testid="stFileUploaderDropzone"]:hover {
        background-color: rgba(255, 255, 255, 0.95) !important;
        border-color: #3B82F6 !important;
        box-shadow: 0 8px 32px rgba(99, 102, 241, 0.2) !important;
    }

    /* តម្រឹមប៊ូតុង និងអក្សរក្នុងប្រអប់ឱ្យចំកណ្តាល */
    div[data-testid="stFileUploaderDropzone"] > div {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 12px !important;
        width: 100% !important;
    }

    /* កែច្នៃប៊ូតុង Browse Files ក្នុងប្រអប់ */
    div[data-testid="stFileUploaderDropzone"] button {
        background: linear-gradient(135deg, #6366F1 0%, #3B82F6 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 10px 24px !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.2) !important;
        font-size: 14px !important;
    }

    /* កែច្នៃពណ៌អក្សរណែនាំក្នុងប្រអប់ឱ្យពណ៌ក្រម៉ៅស្រួលមើលលើផ្ទៃស */
    div[data-testid="stFileUploaderDropzone"] span,
    div[data-testid="stFileUploaderDropzone"] small {
        color: #1E293B !important; /* ពណ៌ប្រផេះចាស់ */
        font-weight: 500 !important;
    }

    /* ---------------------------------------------------------------- */
    /* 🛠️ ផ្នែកកែច្នៃប៊ូតុង Sidebar (SaaS Side Tabs) */
    /* ---------------------------------------------------------------- */
    div[data-testid="stSidebar"] div.stButton > button {
        text-align: left !important;
        justify-content: flex-start !important;
        width: 100% !important;
        border: 1px solid transparent !important;
        padding: 12px 16px !important;
        border-radius: 10px !important;
        font-size: 15px !important;
        font-weight: 500 !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1) !important;
        margin-bottom: -5px !important;
    }

    div[data-testid="stSidebar"] div.stButton > button[kind="secondary"] {
        background-color: transparent !important;
        color: #94A3B8 !important;
    }
    div[data-testid="stSidebar"] div.stButton > button[kind="secondary"]:hover {
        background-color: rgba(255, 255, 255, 0.05) !important;
        color: #F8FAFC !important;
        transform: translateX(2px) !important;
    }

    div[data-testid="stSidebar"] div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, #6366F1 0%, #3B82F6 100%) !important;
        color: #FFFFFF !important;
        font-weight: bold !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.25) !important;
    }

    /* ប៊ូតុង Logout */
    .logout-box button {
        background-color: rgba(239, 68, 68, 0.1) !important;
        color: #F87171 !important;
        border: 1px solid rgba(239, 68, 68, 0.2) !important;
        justify-content: center !important;
    }
    .logout-box button:hover {
        background-color: rgba(239, 68, 68, 0.2) !important;
        color: #EF4444 !important;
    }

    /* ប៊ូតុងលុបឯកសារចោលពណ៌ក្រហម */
    .delete-box button {
        background-color: #EF4444 !important;
        color: white !important;
        border: none !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        padding: 10px !important;
    }
    .delete-box button:hover {
        background-color: #DC2626 !important;
    }

    /* ប៊ូតុងដំណើរការចម្បងក្នុងផ្ទាំងការងារ */
    .main-action-btn button {
        background: linear-gradient(135deg, #6366F1 0%, #3B82F6 100%) !important;
        color: #FFFFFF !important;
        font-weight: 600 !important;
        border-radius: 10px !important;
        padding: 14px 0px !important;
        box-shadow: 0 4px 20px rgba(99, 102, 241, 0.3) !important;
        justify-content: center !important;
    }
    .main-action-btn button:hover {
        background: linear-gradient(135deg, #4F46E5 0%, #2563EB 100%) !important;
        box-shadow: 0 6px 24px rgba(99, 102, 241, 0.45) !important;
    }

    /* កែសម្រួលពណ៌ Selectbox, Text Area */
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

    # --- បង្កើត State សម្រាប់គ្រប់គ្រងផ្ទាំងការងារ (Navigation State) ---
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = "translate"

    # ==========================================
    # របារចំហៀង (Sidebar)
    # ==========================================
    with st.sidebar:
        st.markdown("<h3 style='color: #F8FAFC !important;'>🟢 គណនីរបស់អ្នក</h3>", unsafe_allow_html=True)
        st.success("ស្ថានភាព៖ កំពុងប្រើប្រាស់")
        
        st.write("") 
        st.markdown("<h4 style='color: #94A3B8 !important; margin-bottom: 5px;'>🗺️ ម៉ឺនុយបញ្ជា</h4>", unsafe_allow_html=True)
        
        # ម៉ឺនុយបញ្ជា (SaaS Side Tabs)
        if st.button(
            "🎙️ បកប្រែសំឡេងទៅជាអក្សរ", 
            key="btn_translate", 
            type="primary" if st.session_state.current_tab == "translate" else "secondary",
            use_container_width=True
        ):
            st.session_state.current_tab = "translate"
            st.rerun()
            
        if st.button(
            "⚙️ ការកំណត់ប្រព័ន្ធ", 
            key="btn_settings", 
            type="primary" if st.session_state.current_tab == "settings" else "secondary",
            use_container_width=True
        ):
            st.session_state.current_tab = "settings"
            st.rerun()
        
        st.write("") 
        
        # ប៊ូតុង Logout
        st.markdown('<div class="logout-box">', unsafe_allow_html=True)
        if st.button("ចាកចេញពីប្រព័ន្ធ (Logout)", key="btn_logout", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)

    # ==========================================
    # ផ្ទាំងកណ្តាល (Main Workflow Logic)
    # ==========================================
    
    # ------------------------------------------
    # លក្ខខណ្ឌទី ១៖ ផ្ទាំង "🎙️ បកប្រែសំឡេងទៅជាអក្សរ"
    # ------------------------------------------
    if st.session_state.current_tab == "translate":
        st.markdown('<div class="main-title">ប្រព័ន្ធបកប្រែ Subtitle & សំឡេង</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-title">បម្លែងឯកសារសំឡេង ឬ Subtitle ទៅជាភាសាខ្មែរដោយស្វ័យប្រវត្តិជាមួយ AI</div>', unsafe_allow_html=True)

        # --- ផ្នែកទី ១៖ បញ្ចូលឯកសារ ---
        st.markdown("<h4 style='color: #F8FAFC;'>📂 ជំហានទី ១៖ បញ្ចូលឯកសារ</h4>", unsafe_allow_html=True)
        
        # ប្រើប្រាស់ Key ដើម្បីអាចសម្អាត File Uploader ឡើងវិញបានងាយស្រួល
        uploaded_file = st.file_uploader(
            "សូមទាញឯកសារទម្លាក់ទីនេះ (គាំទ្រ៖ MP3, WAV, M4A, SRT)", 
            type=['mp3', 'wav', 'm4a', 'srt'],
            key="my_uploader_key"
        )
        
        file_type = None
        if uploaded_file:
            file_type = uploaded_file.name.split('.')[-1].lower()
            
            # បង្កើតជួរដេក៖ ឆ្វេងបង្ហាញដំណឹងជោគជ័យ ស្តាំជាប៊ូតុងលុបចោលពណ៌ក្រហម (🗑️ លុបចោល)
            col_success, col_delete = st.columns([5, 1])
            with col_success:
                st.success(f"✅ ឯកសារទទួលបានជោគជ័យ៖ {uploaded_file.name}")
            with col_delete:
                st.markdown('<div class="delete-box">', unsafe_allow_html=True)
                if st.button("🗑️ លុបចោល", use_container_width=True):
                    # លុបឯកសារចោល និង Reset កម្មវិធីឡើងវិញ
                    st.session_state.my_uploader_key = None
                    st.session_state.processing_done = False
                    st.rerun()
                st.markdown('</div>', unsafe_allow_html=True)

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

        st.markdown('<div class="main-action-btn">', unsafe_allow_html=True)
        if st.button("ដំណើរការបម្លែងឯកសារឥឡូវនេះ", key="run_btn", use_container_width=True):
            if not uploaded_file:
                st.warning("⚠️ សូមបញ្ចូលឯកសារនៅ [ជំហានទី ១] សិន មុននឹងបន្ត!")
            else:
                st.info(f"🔄 កំពុងដំណើរការឯកសារ {uploaded_file.name}... សូមរង់ចាំបន្តិច!")
