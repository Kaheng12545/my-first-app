import streamlit as st
import time

def run_subtitle_app():
    # --- 🎨 កូដ CSS ពិសេស៖ បង្ខំកែសម្រួលប្រអប់ Uploader ឱ្យទៅជាចតុកោណកែងធំ និងចំកណ្តាលបេះបិទ (គ្រប់កំណែ Streamlit) ---
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

    /* របារចំហៀង Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #0B0F19 !important;
        border-right: 1px solid rgba(255, 255, 255, 0.05) !important;
    }

    /* ចំណងជើងកម្មវិធី (ភាសាខ្មែរសុទ្ធសាធ) */
    .main-title {
        text-align: center;
        font-family: 'Khmer OS Muol Light', sans-serif !important;
        background: linear-gradient(135deg, #F8FAFC 0%, #94A3B8 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 30px;
        font-weight: bold;
        margin-top: 15px;
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
    /* 🚀 ផ្នែកកូដបង្ខំផ្លុំប្រអប់ Uploader ឱ្យទៅជាចតុកោណកែងធំ និងកណ្តាលបេះបិទ (Core CSS Override) */
    /* ---------------------------------------------------------------- */
    
    /* ១. លុបផ្ទៃខាងក្រោយខ្មៅ និងគែមចាស់ចោលទាំងអស់ */
    .stFileUploader, 
    div[data-testid="stFileUploader"], 
    section[data-testid="stFileUploader"] {
        background-color: transparent !important;
        border: none !important;
        padding: 0px !important;
        display: block !important;
        width: 100% !important;
    }

    /* ២. បង្ខំឱ្យប្រអប់ Dropzone ឡើងរាងជាចតុកោណកែងធំ (កម្ពស់ 280px) និងពណ៌កញ្ចក់សថ្លា */
    .stFileUploader > div,
    div[data-testid="stFileUploaderDropzone"],
    div[data-testid="stFileDropzone"],
    .uploadedFile {
        background-color: rgba(221, 227, 240, 0.95) !important; /* ពណ៌កញ្ចក់សថ្លាស្អាត */
        background: rgba(221, 227, 240, 0.95) !important;
        border: 2px dashed #6366F1 !important; /* គែមឆ្នូតៗពណ៌ស្វាយ */
        border-radius: 16px !important;
        height: 280px !important; /* បង្ខំកម្ពស់រាងចតុកោណកែងធំ */
        min-height: 280px !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important; /* តម្រឹមចំកណ្តាលឆ្វេងស្តាំ */
        justify-content: center !important; /* សម្រួលឱ្យចំកណ្តាលលើក្រោម */
        text-align: center !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2) !important;
        padding: 30px !important;
        transition: all 0.3s ease-in-out !important;
    }

    /* ពេលដាក់ Mouse ពីលើ */
    .stFileUploader > div:hover,
    div[data-testid="stFileUploaderDropzone"]:hover {
        background-color: rgba(255, 255, 255, 0.98) !important;
        background: rgba(255, 255, 255, 0.98) !important;
        border-color: #3B82F6 !important;
        box-shadow: 0 12px 40px rgba(99, 102, 241, 0.25) !important;
    }

    /* ៣. រៀបចំប្លង់ និងរចនាសម្ព័ន្ធខាងក្នុងឱ្យរត់ចំកណ្តាល និងបាត់ឆ្នូតខ្មៅចាស់ */
    div[data-testid="stFileUploaderDropzone"] > div,
    div[data-testid="stFileUploaderDropzone"] > section,
    .stFileUploader > div > div {
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        gap: 15px !important;
        width: 100% !important;
        height: 100% !important;
        background-color: transparent !important;
        background: transparent !important;
        border: none !important;
        padding: 0px !important;
    }

    /* ៤. បង្ខំប៊ូតុង "Browse Files" (Upload) ឱ្យធំ និងចំកណ្តាលចតុកោណកែង */
    div[data-testid="stFileUploaderDropzone"] button,
    .stFileUploader button {
        background: linear-gradient(135deg, #6366F1 0%, #3B82F6 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        padding: 12px 32px !important; /* ប៊ូតុងធំស្អាត */
        border-radius: 8px !important;
        font-weight: bold !important;
        font-size: 15px !important;
        box-shadow: 0 4px 15px rgba(99, 102, 241, 0.3) !important;
        margin: 0 auto !important; /* បង្ខំចំកណ្តាលឆ្វេងស្តាំ */
        display: inline-block !important;
    }

    /* ៥. កែច្នៃរូបតំណាងសញ្ញា Upload (SVG Icon) ឱ្យធំស្អាតចំកណ្តាល */
    div[data-testid="stFileUploaderDropzone"] svg,
    .stFileUploader svg {
        fill: #6366F1 !important;
        width: 50px !important;
        height: 50px !important;
        margin: 0 auto 10px auto !important;
        display: block !important;
    }

    /* ៦. បង្ខំអក្សរណែនាំក្នុងប្រអប់ឱ្យពណ៌ក្រម៉ៅងាយមើលលើផ្ទៃសថ្លា */
    div[data-testid="stFileUploaderDropzone"] span,
    div[data-testid="stFileUploaderDropzone"] small,
    .stFileUploader span,
    .stFileUploader small {
        color: #1E293B !important; 
        font-weight: 500 !important;
        font-size: 14px !important;
        text-align: center !important;
        margin: 0 auto !important;
        display: block !important;
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

    # --- បង្កើត State សម្រាប់គ្រប់គ្រងផ្ទាំងការងារ ---
    if 'current_tab' not in st.session_state:
        st.session_state.current_tab = "translate"

    # ==========================================
    # របារចំហៀង (Sidebar) - លុបប្រអប់ "គណនីរបស់អ្នក" ចេញស្អាតដាច់ស្រឡះ
    # ==========================================
    with st.sidebar:
        st.write("") 
        st.markdown("<h4 style='color: #94A3B8 !important; margin-bottom: 10px;'>🗺️ ម៉ឺនុយបញ្ជា</h4>", unsafe_allow_html=True)
        
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
        # ផ្លាស់ប្តូរចំណងជើងជាភាសាខ្មែរសុទ្ធសាធ និងលុបអក្សរអង់គ្លេសចោលទាំងស្រុង
        st.markdown('<div class="main-title">ប្រព័ន្ធបកប្រែពីសំឡេងទៅជាអក្សរ</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-title">បម្លែងរាល់ឯកសារសំឡេងទៅជាអក្សរខ្មែរដោយស្វ័យប្រវត្តិជាមួយ AI</div>', unsafe_allow_html=True)

        # --- ផ្នែកទី ១៖ បញ្ចូលឯកសារ ---
        st.markdown("<h4 style='color: #F8FAFC;'>📂 ជំហានទី ១៖ បញ្ចូលឯកសារ</h4>", unsafe_allow_html=True)
        
        # ប្រអប់អាប់ឡូតដែលមានទំហំជាចតុកោណកែងធំ
        uploaded_file = st.file_uploader(
            "សូមទាញឯកសារទម្លាក់ទីនេះ (គាំទ្រ៖ MP3, WAV, M4A, SRT)", 
            type=['mp3', 'wav', 'm4a', 'srt'],
            key="my_uploader_key"
        )
        
        file_type = None
        if uploaded_file:
            file_type = uploaded_file.name.split('.')[-1].lower()
            
            # ប៊ូតុងលុបចោលពណ៌ក្រហម (🗑️ លុបចោល)
            col_success, col_delete = st.columns([5, 1])
            with col_success:
                st.success(f"✅ ឯកសារទទួលបានជោគជ័យ៖ {uploaded_file.name}")
            with col_delete:
                st.markdown('<div class="delete-box">', unsafe_allow_html=True)
                if st.button("🗑️ លុបចោល", use_container_width=True):
                    # លុបឯកសារចោល និង Reset ប្រព័ន្ធឡើងវិញ
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
                
                progress_bar = st.progress(0)
                with st.spinner("ប្រព័ន្ធ AI កំពុងដំណើរការ..."):
                    for i in range(1, 101, 20):
                        time.sleep(0.4)
                        progress_bar.progress(i)
                    
                st.success("🎉 ដំណើរការបកប្រែជោគជ័យ!")
                st.session_state.processing_done = True
        st.markdown('</div>', unsafe_allow_html=True)
                
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
    elif st.session_state.current_tab == "settings":
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
