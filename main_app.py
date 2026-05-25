import streamlit as st
import time

def run_subtitle_app():
    # --- 🎨 កំណត់ Font អក្សរខ្មែរឱ្យស្អាតគ្រប់ជ្រុងទាំងអស់ ---
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

    /* បន្ថែមរចនាបថលើ Tabs ឱ្យកាន់តែស្អាត */
    button[data-baseweb="tab"] {
        font-family: 'Kantumruy Pro', sans-serif !important;
        font-weight: bold !important;
        font-size: 16px !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # ==========================================
    # របារចំហៀង (Sidebar) - រក្សាទុកដដែលទាំងស្រុង
    # ==========================================
    with st.sidebar:
        st.markdown("### 🟢 គណនីរបស់អ្នក")
        st.success("ស្ថានភាព៖ កំពុងប្រើប្រាស់")
        
        # បន្ថែម Line break ឱ្យស្រឡះភ្នែក
        st.write("") 
        if st.button("ចាកចេញពីប្រព័ន្ធ (Logout)", use_container_width=True):
            st.session_state.logged_in = False
            st.rerun()

    # ==========================================
    # ផ្ទាំងកណ្តាល (Main Workflow)
    # ==========================================
    st.markdown('<div class="main-title">ប្រព័ន្ធបកប្រែ Subtitle & សំឡេង</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">bម្លែងឯកសារសំឡេង ឬ Subtitle ទៅជាភាសាខ្មែរដោយស្វ័យប្រវត្តិជាមួយ AI</div>', unsafe_allow_html=True)

    # បង្កើតប៊ូតុង Tab នៅផ្នែកខាងលើ
    tab_translate, tab_settings = st.tabs(["🎙️ បកប្រែសំឡេងទៅជាអក្សរ", "⚙️ ការកំណត់"])

    # ------------------------------------------
    # Tab ទី ១៖ ផ្ទាំងការងារបកប្រែ (រក្សាទុកកូដចាស់បងទាំងអស់)
    # ------------------------------------------
    with tab_translate:
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
        
        # បង្កើត state សម្រាប់រក្សាទុកលទ្ធផលកុំឱ្យបាត់ពេលទាញយក (Download)
        if 'processing_done' not in st.session_state:
            st.session_state.processing_done = False

        if st.button("ដំណើរការបម្លែងឯកសារឥឡូវនេះ", type="primary", use_container_width=True):
            if not uploaded_file:
                st.warning("⚠️ សូមបញ្ចូលឯកសារនៅ [ជំហានទី ១] សិន មុននឹងបន្ត!")
            else:
                st.info(f"🔄 កំពុងដំណើរការឯកសារ {uploaded_file.name}... សូមរង់ចាំបន្តិច!")
                
                # បង្កើត Spinner ត្រាប់តាមការងារពិត
                progress_bar = st.progress(0)
                with st.spinner("ប្រព័ន្ធ AI កំពុងធ្វើការបកប្រែ..."):
                    for i in range(1, 101, 20):
                        time.sleep(0.4)  # ធ្វើពុតជាកំពុងដំណើរការ
                        progress_bar.progress(i)
                    
                st.success("🎉 ដំណើរការបកប្រែជោគជ័យ! (ត្រៀមចូលវគ្គកូដ AI ពិតប្រាកដ)")
                st.session_state.processing_done = True

        # --- ផ្នែកទី ៤៖ បង្ហាញលទ្ធផល និងទាញយក ---
        if st.session_state.processing_done and uploaded_file:
            st.divider()
            st.markdown("#### 📄 លទ្ធផលទទួលបានពី AI (គំរូ)")
            
            # ឧទាហរណ៍អត្ថបទដែលបកប្រែរួច
            sample_translated_text = (
                "1\n00:00:01,000 --> 00:00:04,000\nសួស្តីអ្នកទាំងអស់គ្នា! សូមស្វាគមន៍មកកាន់ការទស្សនា។\n\n"
                "2\n00:00:04,500 --> 00:00:08,000\nថ្ងៃនេះយើងនឹងជជែកគ្នាអំពីបច្គេកវិទ្យាបញ្ញាសិប្បនិម្មិត AI។"
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
    # Tab ទី ២៖ ផ្ទាំងការកំណត់ (ផ្ទាំងសស្អាតថ្មីតាមការចង់បាន)
    # ------------------------------------------
    with tab_settings:
        st.markdown("#### ⚙️ ការកំណត់ប្រព័ន្ធ (System Settings)")
        st.write("សូមកំណត់តម្លៃផ្សេងៗសម្រាប់ដំណើរការម៉ាស៊ីន AI របស់អ្នកនៅទីនេះ៖")
        
        # បង្កើត Form សម្រាប់កំណត់ Keys ផ្សេងៗ
        with st.form("settings_form"):
            st.markdown("##### 🔑 គ្រាប់ចុចសម្ងាត់ (API Keys)")
            gemini_key = st.text_input("Google Gemini API Key:", type="password", placeholder="AIzaSy...")
            openai_key = st.text_input("OpenAI API Key:", type="password", placeholder="sk-proj-...")
            
            st.markdown("##### 🌍 ការកំណត់ភាសា និងដំណើរការ")
            target_lang = st.selectbox("ភាសាគោលដៅសម្រាប់ការបកប្រែ៖", ["ភាសាខ្មែរ (Khmer)", "ភាសាអង់គ្លេស (English)"])
            temperature = st.slider("កម្រិតភាពច្នៃប្រឌិតរបស់ AI (Temperature):", min_value=0.0, max_value=1.0, value=0.3, step=0.1)
            
            submit_btn = st.form_submit_button("រក្សាទុកការកំណត់")
            if submit_btn:
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
