import streamlit as st
import time

def run_subtitle_app():
    # --- 🎨 កំណត់ CSS តាមស្ទីល Transkriptor Glassmorphism (Theme របស់បង) ---
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Khmer+OS+Muol+Light&family=Kantumruy+Pro:wght@300;400;700&display=swap');
    
    /* 1. កំណត់ Font ទូទៅ */
    html, body, [class*="css"], [class*="st-"], p, span, div, label, li, button, input, select, textarea {
        font-family: 'Kantumruy Pro', sans-serif !important;
    }

    /* 2. កំណត់ពណ៌ផ្ទៃខាងក្រោយកម្មវិធីទាំងមូល (Theme: bg) */
    .stApp {
        background: linear-gradient(135deg, #A8B3C7 0%, #DDE3F0 100%) !important;
    }

    /* 3. កំណត់ពណ៌របារចំហៀង Sidebar (Theme: glass) */
    section[data-testid="stSidebar"] {
        background-color: rgba(221, 227, 240, 0.85) !important;
        backdrop-filter: blur(15px) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.4) !important;
    }

    /* 4. កំណត់ចំណងជើងជាពណ៌ស (Theme: text) ឱ្យលេចធ្លោ */
    h1, h2, h3, h4, h5, h6, .main-title {
        font-family: 'Khmer OS Muol Light', sans-serif !important;
        color: #FFFFFF !important;
        text-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .main-title {
        text-align: center;
        font-size: 32px;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        font-size: 15px;
        color: #FFFFFF !important;
        opacity: 0.9;
        margin-bottom: 30px;
    }

    /* 5. កែច្នៃប្រអប់ Form និងកន្លែងបញ្ចូលឯកសារឱ្យទៅជាកញ្ចក់ថ្លា (Theme: glass) */
    div[data-testid="stForm"], 
    .stFileUploader, 
    div[data-testid="stNotification"] {
        background-color: rgba(221, 227, 240, 0.7) !important;
        backdrop-filter: blur(12px) !important;
        border-radius: 16px !important;
        border: 1px solid rgba(255, 255, 255, 0.5) !important;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.08) !important;
        padding: 20px !important;
    }

    /* 6. កែច្នៃប៊ូតុងក្នុង Sidebar (Menu Selection) */
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] label {
        background-color: #EEF2FF !important; /* Theme: button */
        color: #2C3E50 !important;
        border: 1px solid rgba(255, 255, 255, 0.6) !important;
        border-radius: 10px !important;
        padding: 12px 16px !important;
        cursor: pointer;
        transition: 0.2s;
        width: 100%;
    }
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
        background-color: #DDE3F0 !important;
        transform: translateY(-1px);
    }
    /* ម៉ឺនុយដែលបានជ្រើសរើស (Theme: accent) */
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
        background-color: #60A5FA !important; 
        border-color: #60A5FA !important;
    }
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] span {
        color: #FFFFFF !important;
        font-weight: bold !important;
    }
    /* លាក់រង្វង់មូលនៃ Radio Button */
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] [data-testid="stHighlightContainer"] {
        display: none !important;
    }
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] label div:first-child {
        display: none !important;
    }

    /* 7. កែច្នៃប៊ូតុងដំណើរការចម្បង (Theme: accent & text) */
    div.stButton > button:first-child {
        width: 100%;
        background-color: #60A5FA !important; /* Theme: accent */
        color: #FFFFFF !important; /* Theme: text */
        font-family: 'Kantumruy Pro', sans-serif !important;
        font-weight: bold !important;
        border-radius: 10px !important;
        padding: 12px 0px !important;
        font-size: 16px !important;
        transition: 0.3s;
        border: none !important;
        box-shadow: 0 4px 15px rgba(96, 165, 250, 0.3) !important;
    }
    div.stButton > button:first-child:hover {
        background-color: #3B82F6 !important;
        transform: translateY(-1px);
    }

    /* ប៊ូតុង Logout (ពណ៌ទន់ភ្លន់) */
    div[data-testid="stSidebar"] button {
        background-color: #EEF2FF !important;
        color: #EF4444 !important;
        border: 1px solid rgba(239, 68, 68, 0.2) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # ==========================================
    # របារចំហៀង (Sidebar)
    # ==========================================
    with st.sidebar:
        st.markdown("<h3 style='color: #2C3E50 !important;'>🟢 គណនីរបស់អ្នក</h3>", unsafe_allow_html=True)
        st.success("ស្ថានភាព៖ កំពុងប្រើប្រាស់")
        
        st.write("") 
        
        # 🎯 ម៉ឺនុយបញ្ជាផ្ទាំងការងារ (ស្ថិតនៅក្នុង Sidebar តាមស្នើសុំរបស់បង)
        st.markdown("<h4 style='color: #2C3E50 !important;'>🗺️ ម៉ឺនុយបញ្ជា</h4>", unsafe_allow_html=True)
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
        st.markdown("#### 📂 ជំហានទី ១៖ បញ្ចូលឯកសារ")
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
        st.markdown("#### 🤖 ជំហានទី ២៖ ជ្រើសរើសម៉ូដែល AI")
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
        st.markdown("#### 🚀 ជំហានទី ៣៖ ចាប់ផ្ដើមប្រតិបត្តិការ")
        
        if 'processing_done' not in st.session_state:
            st.session_state.processing_done = False

        if st.button("ដំណើរការបម្លែងឯកសារឥឡូវនេះ", type="primary", use_container_width=True):
            if not uploaded_file:
                st.warning("⚠️ សូមបញ្ចូលឯកសារនៅ [ជំហានទី ១] សិន មុននឹងបន្ត!")
            else:
                st.info(f"🔄 កំពុងដំណើរការឯកសារ {uploaded_file.name}... សូមរង់ចាំបន្តិច!")
                
                # បង្កើត Progress bar ស្អាត
                progress_bar = st.progress(0)
                with st.spinner("ប្រព័ន្ធ AI កំពុងដំណើរការ..."):
                    for i in range(1, 101, 20):
                        time.sleep(0.5)
                        progress_bar.progress(i)
                    
                st.success("🎉 ដំណើរការបកប្រែជោគជ័យ!")
                st.session_state.processing_done = True
                
        # --- ផ្នែកទី ៤៖ បង្ហាញលទ្ធផល និងទាញយក ---
        if st.session_state.processing_done and uploaded_file:
            st.divider()
            st.markdown("#### 📄 លទ្ធផលទទួលបានពី AI (គំរូ)")
            
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
            st.markdown("#### ⚙️ កម្រងព័ត៌មាន និង API Keys")
            
            with st.form("settings_form"):
                st.text_input("🔑 Google Gemini API Key:", type="password", placeholder="បញ្ចូល API Key របស់ Gemini នៅទីនេះ")
                st.text_input("🔑 OpenAI API Key:", type="password", placeholder="បញ្ចូល API Key របស់ OpenAI នៅទីនេះ")
                
                st.divider()
                st.markdown("##### ⚙️ ការកំណត់ទូទៅ")
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
