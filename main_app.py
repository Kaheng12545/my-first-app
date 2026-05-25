import streamlit as st
import time

def run_subtitle_app():
    # --- 🎨 កំណត់ Font អក្សរខ្មែរ និង CSS តុបតែង Sidebar Menu ---
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Khmer+OS+Muol+Light&family=Kantumruy+Pro:wght@300;400;700&display=swap');
    
    /* កំណត់អក្សរទូទៅទាំងអស់ឱ្យប្រើ Kantumruy Pro */
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
        font-size: 30px;
        margin-bottom: 5px;
    }
    .sub-title {
        text-align: center;
        font-family: 'Kantumruy Pro', sans-serif !important;
        font-size: 15px;
        color: #5F6368 !important;
        margin-bottom: 30px;
    }
    
    /* រចនាប៊ូតុងដំណើរការឱ្យធំ លេចធ្លោ */
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

    /* 🛠️ កែច្នៃវិទ្យុ (Radio Button) ក្នុង Sidebar ឱ្យទៅជាប៊ូតុងម៉ឺនុយបញ្ជាស្អាត */
    div[data-testid="stSidebar"] div[data-testid="stRadio"] {
        padding: 10px 0px;
    }
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] {
        gap: 10px;
        flex-direction: column;
    }
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] label {
        background-color: #f0f2f6;
        padding: 12px 16px !important;
        border-radius: 8px !important;
        border: 1px solid #e0e0e0;
        cursor: pointer;
        transition: all 0.2s ease-in-out;
        width: 100%;
    }
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] label:hover {
        background-color: #e4e6eb;
        border-color: #ccd0d5;
    }
    /* នៅពេលចុចជ្រើសរើស ឱ្យវាឡើងពណ៌ខៀវលេចធ្លោ */
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] {
        background-color: #1a73e8 !important;
        border-color: #1a73e8 !important;
    }
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] label[data-checked="true"] span {
        color: white !important;
        font-weight: bold !important;
    }
    /* លាក់រង្វង់មូលមូលនៃ Radio Button */
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] [data-testid="stHighlightContainer"] {
        display: none !important;
    }
    div[data-testid="stSidebar"] div[data-testid="stRadio"] div[role="radiogroup"] label div:first-child {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # ==========================================
    # របារចំហៀង (Sidebar)
    # ==========================================
    with st.sidebar:
        st.markdown("### 🟢 គណនីរបស់អ្នក")
        st.success("ស្ថានភាព៖ កំពុងប្រើប្រាស់")
        
        st.write("") # បន្ថែមគម្លាត
        
        # 🎯 ម៉ឺនុយបញ្ជាផ្ទាំងការងារ (ស្ថិតនៅក្នុង Sidebar តាមស្នើសុំរបស់បង)
        st.markdown("#### 🗺️ ម៉ឺនុយបញ្ជា")
        menu_option = st.radio(
            "សូមជ្រើសរើសផ្ទាំង៖",
            ["🎙️ បកប្រែសំឡេងទៅជាអក្សរ", "⚙️ ការកំណត់"],
            label_visibility="collapsed" # លាក់ចំណងជើងសរសេរដើម្បីកុំឱ្យរញ៉េរញ៉ៃ
        )
        
        # បន្ថែម Line break ឱ្យស្រឡះភ្នែក
        st.write("") 
        if st.button("ចាកចេញពីប្រព័ន្ធ (Logout)", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

    # ==========================================
    # ផ្ទាំងកណ្តាល (Main Workflow Logic)
    # ==========================================
    
    # ------------------------------------------
    # លក្ខខណ្ឌទី ១៖ ប្រសិនបើជ្រើសរើស "🎙️ បកប្រែសំឡេងទៅជាអក្សរ"
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
            # បើឯកសារជា SRT មិនចាំបាច់ប្រើម៉ូដែលស្ដាប់សំឡេងឡើយ
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
                
                # បង្កើត Spinner ត្រាប់តាមការងារពិត
                progress_bar = st.progress(0)
                with st.spinner("ប្រព័ន្ធ AI កំពុងដំណើរការ..."):
                    for i in range(1, 101, 20):
                        time.sleep(0.5)  # ធ្វើពុតជាកំពុងដំណើរការ
                        progress_bar.progress(i)
                    
                st.success("🎉 ដំណើរការបកប្រែជោគជ័យ!")
                st.session_state.processing_done = True
                
        # --- ផ្នែកទី ៤៖ បង្ហាញលទ្ធផល និងទាញយក ---
        if st.session_state.processing_done and uploaded_file:
            st.divider()
            st.markdown("#### 📄 លទ្ធផលទទួលបានពី AI (គំរូ)")
            
            # ឧទាហរណ៍អត្ថបទដែលបកប្រែរួច
            sample_translated_text = (
                "1\n00:00:01,000 --> 00:00:04,000\nសួស្តីអ្នកទាំងអស់គ្នា! សូមស្វាគមន៍មកកាន់ការទស្សនា។\n\n"
                "2\n00:00:04,500 --> 00:00:08,000\nថ្ងៃនេះយើងនឹងជជែកគ្នាអំពីបច្ចេកវិទ្យាបញ្ញាសិប្បនិម្មិត AI។"
            )
            
            st.text_area("អត្ថបទ Subtitle ជាភាសាខ្មែរ៖", value=sample_translated_text, height=150)
            
            # ប៊ូតុងទាញយកឯកសារ
            st.download_button(
                label="📥 ទាញយកឯកសារបកប្រែរួច (.srt)",
                data=sample_translated_text,
                file_name=f"translated_{uploaded_file.name.split('.')[0]}.srt",
                mime="text/plain",
                use_container_width=True
            )

    # ------------------------------------------
    # លក្ខខណ្ឌទី ២៖ ប្រសិនបើជ្រើសរើស "⚙️ ការកំណត់"
    # ------------------------------------------
    elif menu_option == "⚙️ ការកំណត់":
        # ផ្ទាំងទទេស្អាតសម្រាប់កូដកំណត់ប្រព័ន្ធ (Settings)
        st.markdown('<div class="main-title">ការកំណត់ប្រព័ន្ធ</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-title">គ្រប់គ្រងគណនី និងការកំណត់ API សម្រាប់ការបកប្រែ</div>', unsafe_allow_html=True)
        
        with st.container():
            st.markdown("#### ⚙️ កម្រងព័ត៌មាន និង API Keys")
            
            # បង្កើតប្រអប់បញ្ចូលទិន្នន័យស្អាតៗ
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
    # បង្កើត session_state ជាគំរូសម្រាប់ការតេស្ត
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = True
        
    if st.session_state.logged_in:
        run_subtitle_app()
    else:
        st.write("សូមចូលប្រព័ន្ធម្តងទៀត។")
