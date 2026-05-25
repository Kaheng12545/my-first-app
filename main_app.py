import streamlit as st
import time

def run_subtitle_app():
    # =========================================================================
    # 🎨 វគ្គទី ១៖ កូដ CSS ជួសជុលរូបរាង (អក្សរខ្មៅច្បាស់ៗ, ប៊ូតុងស្អាត)
    # =========================================================================
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Khmer+OS+Muol+Light&family=Kantumruy+Pro:wght@300;400;500;700&display=swap');
    
    html, body, [class*="css"], [class*="st-"], p, span, div, label, li, button, input, select, textarea {
        font-family: 'Kantumruy Pro', sans-serif !important;
        color: #1E293B !important; /* បង្ខំឱ្យអក្សរទាំងអស់មានពណ៌ខ្មៅ ងាយមើល */
    }
    
    .stApp { background-color: #F8FAFC !important; }
    
    .main-title {
        text-align: center;
        font-family: 'Khmer OS Muol Light', sans-serif !important;
        color: #1E3A8A !important;
        font-size: 30px;
        margin-top: 10px;
        margin-bottom: 30px;
    }

    /* ប្រអប់ខ្មៅបង្ហាញឈ្មោះហ្វាលនៅខាងឆ្វេង */
    .filename-box {
        background-color: #111827 !important;
        border: 2px dashed #334155 !important; 
        border-radius: 12px !important; 
        height: 60px !important; 
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 0 20px !important;
        font-family: 'Kantumruy Pro', monospace !important;
        font-size: 16px !important; 
        overflow: hidden !important;
        white-space: nowrap !important;
        text-overflow: ellipsis !important;
    }

    /* ជួសជុល និងលាក់ប្រអប់ Uploader ចាស់ចោល */
    [data-testid="stFileUploader"] { margin-bottom: 0 !important; }
    [data-testid="stFileUploaderDropzone"] {
        border: none !important;
        background-color: transparent !important;
        padding: 0 !important;
        min-height: 60px !important; 
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    [data-testid="stFileUploaderDropzone"] > div > div, 
    [data-testid="stFileUploaderDropzone"] small { display: none !important; }

    /* ប៊ូតុង "បញ្ចូលហ្វាល" នៅខាងស្តាំ */
    [data-testid="stFileUploaderDropzone"] > button {
        background-color: #3B82F6 !important;
        border: none !important;
        border-radius: 12px !important;
        height: 60px !important; 
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        cursor: pointer !important;
        color: transparent !important; 
        font-size: 0px !important; 
        position: relative !important;
    }
    [data-testid="stFileUploaderDropzone"] > button:hover { background-color: #2563EB !important; }
    
    [data-testid="stFileUploaderDropzone"] > button::after {
        content: "➕ បញ្ចូលហ្វាល" !important;
        font-family: 'Kantumruy Pro', sans-serif !important;
        font-size: 18px !important; 
        font-weight: bold !important;
        color: white !important;
        position: absolute !important;
        top: 0; left: 0; right: 0; bottom: 0;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }

    /* ប៊ូតុងលុបហ្វាល (ក្រោយពេល Upload) */
    [data-testid="stFileUploaderFileData"] {
        background-color: #EF4444 !important;
        height: 60px !important;
        border-radius: 12px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        padding: 0 !important; margin: 0 !important;
    }
    [data-testid="stFileUploaderFileData"]::after {
        content: "🗑️ លុបហ្វាលចេញ" !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: bold !important;
        position: absolute !important;
        pointer-events: none !important;
    }
    [data-testid="stFileUploaderFileData"] button {
        opacity: 0 !important; width: 100% !important; height: 100% !important; cursor: pointer !important;
    }
    [data-testid="stFileUploaderFileData"] div[data-testid="stMarkdownContainer"] { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

    # --- ចំណងជើងកម្មវិធី ---
    st.markdown('<div class="main-title">🎙️ កម្មវិធីបម្លែងសំឡេងទៅជាអក្សរ (Subtitle)</div>', unsafe_allow_html=True)

    # =========================================================================
    # 📂 វគ្គទី ២៖ បញ្ចូលឯកសារ (ប្រអប់ខ្មៅ និង ប៊ូតុងខៀវ)
    # =========================================================================
    st.markdown("### 📂 ជំហានទី ១៖ បញ្ចូលឯកសារសំឡេង ឬវីដេអូ")
    col_box, col_btn = st.columns([2.5, 1.5])

    with col_btn:
        uploaded_file = st.file_uploader("", label_visibility="collapsed")

    with col_box:
        if uploaded_file:
            st.markdown(f'<div class="filename-box" style="color: #10B981; border-color: #10B981;">✅ {uploaded_file.name}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="filename-box" style="color: #94A3B8;">មិនទាន់មានឯកសារទេ...</div>', unsafe_allow_html=True)

    st.divider()

    # =========================================================================
    # ⚙️ វគ្គទី ៣៖ ការកំណត់ភាសា និង ទម្រង់ឯកសារ
    # =========================================================================
    st.markdown("### ⚙️ ជំហានទី ២៖ កំណត់ភាសា និង ទម្រង់ឯកសារ")
    
    col1, col2 = st.columns(2)
    with col1:
        target_lang = st.selectbox("🌍 ជ្រើសរើសភាសាដែលចង់បកប្រែទៅជា៖", ["🇰🇭 ភាសាខ្មែរ (Khmer)", "🇬🇧 អង់គ្លេស (English)", "🇹🇭 ថៃ (Thai)"])
    with col2:
        output_format = st.selectbox("📄 ជ្រើសរើសទម្រង់ឯកសារដែលចង់បាន៖", ["ឯកសារ Subtitle (.SRT)", "អត្ថបទធម្មតា (.TXT)"])

    st.divider()

    # =========================================================================
    # 🚀 វគ្គទី ៤៖ ចាប់ផ្តើមដំណើរការ (Progress Bar ដើររលូន)
    # =========================================================================
    st.markdown("### 🚀 ជំហានទី ៣៖ ចាប់ផ្តើមបម្លែង")

    if 'processing_done' not in st.session_state:
        st.session_state.processing_done = False
    if 'final_text' not in st.session_state:
        st.session_state.final_text = ""

    if st.button("⚡ ចាប់ផ្តើមដំណើរការបកប្រែ", type="primary", use_container_width=True):
        if not uploaded_file:
            st.warning("⚠️ សូមបញ្ចូលឯកសារនៅ ជំហានទី ១ សិន!")
        else:
            progress_bar = st.progress(0)
            status_text = st.empty()

            # ដំណើរការក្លែងធ្វើ (Simulation) ដើររលូនដូចទឹក
            for i in range(101):
                if i < 30:
                    time.sleep(0.02)
                    status_text.markdown("🔄 កំពុងទាញយកសំឡេងពីឯកសារ...")
                elif i < 60:
                    time.sleep(0.04)
                    status_text.markdown("🤖 AI កំពុងស្តាប់ និងវិភាគសំឡេង...")
                elif i < 90:
                    time.sleep(0.05)
                    status_text.markdown(f"✨ កំពុងបកប្រែទៅជា {target_lang}...")
                else:
                    time.sleep(0.02)
                    status_text.markdown("✅ កំពុងរៀបចំឯកសារចុងក្រោយ...")
                progress_bar.progress(i)

            status_text.success("🎉 ដំណើរការចប់សព្វគ្រប់ ១០០%!")
            
            # ទិន្នន័យគំរូដែលចេញមក
            if "SRT" in output_format:
                st.session_state.final_text = "1\n00:00:01,000 --> 00:00:05,000\nសួស្តីអ្នកទាំងអស់គ្នា!\n\n2\n00:00:05,500 --> 00:00:09,000\nសូមស្វាគមន៍មកកាន់វីដេអូនេះ។"
                st.session_state.file_ext = "srt"
            else:
                st.session_state.final_text = "សួស្តីអ្នកទាំងអស់គ្នា! សូមស្វាគមន៍មកកាន់វីដេអូនេះ។"
                st.session_state.file_ext = "txt"
                
            st.session_state.processing_done = True

    # =========================================================================
    # 📥 វគ្គទី ៥៖ បង្ហាញ និងទាញយក
    # =========================================================================
    if st.session_state.processing_done and uploaded_file:
        st.markdown(f"### 📄 លទ្ធផលទទួលបាន ({output_format})")
        
        st.text_area("មើលអត្ថបទជាមុន៖", value=st.session_state.final_text, height=200)
        
        st.download_button(
            label=f"📥 ទាញយកឯកសារ .{st.session_state.file_ext.upper()}",
            data=st.session_state.final_text,
            file_name=f"Translated_File.{st.session_state.file_ext}",
            mime="text/plain",
            use_container_width=True
        )

if __name__ == "__main__":
    run_subtitle_app()
