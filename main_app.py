import streamlit as st
import tempfile
import os
import time
from openai import OpenAI

def run_subtitle_app():
    # =========================================================================
    # 🛠️ ជួសជុល Error: ប្រកាស State ទុកជាមុនកុំឱ្យលោតក្រហម
    # =========================================================================
    if 'processing_done' not in st.session_state:
        st.session_state.processing_done = False
    if 'final_srt' not in st.session_state:
        st.session_state.final_srt = ""

    # =========================================================================
    # 🎨 វគ្គទី ១៖ កូដ CSS រចនា UI ដ៏ស្រស់ស្អាត (ដែលយើងខំធ្វើពេញមួយថ្ងៃ)
    # =========================================================================
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Khmer+OS+Muol+Light&family=Kantumruy+Pro:wght@300;400;500;700&display=swap');
    
    html, body, [class*="css"], [class*="st-"], p, span, div, label, li, button, input, select, textarea {
        font-family: 'Kantumruy Pro', sans-serif !important;
    }
    
    .stApp { background-color: #F8FAFC !important; }
    
    .main-title {
        text-align: center;
        font-family: 'Khmer OS Muol Light', sans-serif !important;
        color: #1E3A8A;
        font-size: 30px;
        margin-top: 10px;
        margin-bottom: 20px;
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
        text-align: center !important;
        padding: 0 20px !important;
        font-family: 'Kantumruy Pro', monospace !important;
        font-size: 16px !important; 
        overflow: hidden !important;
        white-space: nowrap !important;
        text-overflow: ellipsis !important;
        box-shadow: inset 0 4px 10px rgba(0,0,0,0.3) !important;
        margin-top: 2px !important;
    }

    /* កម្ទេចអក្សរ Uploader ចាស់ៗ */
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

    /* ប៊ូតុង Add File នៅខាងស្តាំ */
    [data-testid="stFileUploaderDropzone"] > button {
        background-color: #3B82F6 !important;
        border: none !important;
        border-radius: 12px !important;
        height: 60px !important; 
        width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
        cursor: pointer !important;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4) !important;
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

    /* ប៊ូតុង Remove File ពណ៌ក្រហម */
    [data-testid="stFileUploaderFileData"] {
        position: relative !important;
        width: 100% !important;
        height: 60px !important;
        background-color: #EF4444 !important;
        border-radius: 12px !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0 !important;
        padding: 0 !important;
    }
    [data-testid="stFileUploaderFileData"]:hover { background-color: #DC2626 !important; }
    
    [data-testid="stFileUploaderFileData"]::after {
        content: "🗑️ លុបហ្វាលចេញ" !important;
        color: white !important;
        font-size: 18px !important;
        font-weight: bold !important;
        font-family: 'Kantumruy Pro', sans-serif !important;
        position: absolute !important;
        pointer-events: none !important;
    }
    [data-testid="stFileUploaderFileData"] button {
        position: absolute !important;
        width: 100% !important;
        height: 100% !important;
        top: 0 !important; left: 0 !important;
        opacity: 0 !important; cursor: pointer !important; z-index: 10 !important;
    }
    [data-testid="stFileUploaderFileData"] div[data-testid="stMarkdownContainer"] { display: none !important; }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-title">🎙️ កម្មវិធីបម្លែងសំឡេងទៅជា Subtitle ខ្មែរ (SRT)</div>', unsafe_allow_html=True)

    # =========================================================================
    # 🔑 វគ្គទី ២៖ បញ្ចូល API Key
    # =========================================================================
    st.markdown("### 🔑 ជំហានទី ១៖ បញ្ចូល OpenAI API Key")
    api_key = st.text_input("បញ្ចូល API Key របស់អ្នកទីនេះ (ចាំបាច់)", type="password")
    if not api_key:
        st.warning("⚠️ ប្រព័ន្ធត្រូវការ API Key ដើម្បីដំណើរការម៉ាស៊ីន AI ពិតប្រាកដ។")
    st.divider()

    # =========================================================================
    # 📂 វគ្គទី ៣៖ UI បញ្ចូលឯកសារ (ប្រអប់ខ្មៅ និង ប៊ូតុងខៀវ)
    # =========================================================================
    st.markdown("### 📂 ជំហានទី ២៖ បញ្ចូលឯកសារសំឡេង")
    col_box, col_btn = st.columns([2.5, 1.5])

    with col_btn:
        uploaded_file = st.file_uploader("", label_visibility="collapsed")

    with col_box:
        if uploaded_file:
            st.markdown(f'<div class="filename-box" style="color: #10B981; border-color: #10B981;">✅ {uploaded_file.name}</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="filename-box" style="color: #64748B;">មិនទាន់មានឯកសារទេ...</div>', unsafe_allow_html=True)

    # ឆែកហ្វាល
    allowed_extensions = ['mp3', 'wav', 'm4a', 'mp4']
    if uploaded_file:
        file_ext = uploaded_file.name.split('.')[-1].lower()
        if file_ext not in allowed_extensions:
            st.error("❌ ប្រព័ន្ធទទួលតែឯកសារសំឡេង និងវីដេអូ (MP3, WAV, M4A, MP4) ប៉ុណ្ណោះ។")
            uploaded_file = None 
    st.divider()

    # =========================================================================
    # 🚀 វគ្គទី ៤៖ ដំណើរការម៉ាស៊ីន AI ពេញលេញ (Backend)
    # =========================================================================
    st.markdown("### 🚀 ជំហានទី ៣៖ ចាប់ផ្តើមបម្លែងជាអក្សរខ្មែរ")

    if st.button("⚡ ចាប់ផ្តើមដំណើរការឥឡូវនេះ", type="primary", use_container_width=True):
        if not api_key:
            st.error("❌ សូមបញ្ចូល API Key នៅជំហានទី ១ សិន!")
        elif not uploaded_file:
            st.error("❌ សូមបញ្ចូលឯកសារនៅជំហានទី ២ សិន!")
        else:
            try:
                # ១. ដាស់ម៉ាស៊ីន AI
                client = OpenAI(api_key=api_key)
                progress_bar = st.progress(0)
                status_text = st.empty()

                # ២. រក្សាទុកហ្វាលចូល RAM
                status_text.info("🔄 កំពុងទាញយកឯកសារ...")
                progress_bar.progress(10)
                
                with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_file_path = tmp_file.name

                # ៣. ស្តាប់ និងទាញ Timestamps តាមរយៈ Whisper
                status_text.info("🤖 ម៉ាស៊ីន AI កំពុងស្តាប់សំឡេង... (សូមរង់ចាំ)")
                progress_bar.progress(40)
                
                with open(tmp_file_path, "rb") as audio_file:
                    transcript_srt = client.audio.transcriptions.create(
                        model="whisper-1", 
                        file=audio_file, 
                        response_format="srt"
                    )
                
                # ៤. បកប្រែជាភាសាខ្មែរតាមរយៈ GPT-4o
                status_text.info("✨ កំពុងបកប្រែជាភាសាខ្មែរ យ៉ាងរលូន...")
                progress_bar.progress(70)

                prompt = "You are a professional Subtitle Translator. Translate the following SRT file to Khmer natively. DO NOT change the timestamps or formatting."
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": prompt},
                        {"role": "user", "content": transcript_srt}
                    ],
                    temperature=0.3 
                )
                
                # ៥. បញ្ចប់
                st.session_state.final_srt = response.choices[0].message.content
                os.remove(tmp_file_path)
                
                progress_bar.progress(100)
                status_text.success("🎉 ដំណើរការចប់សព្វគ្រប់ ១០០%!")
                st.session_state.processing_done = True

            except Exception as e:
                st.error(f"❌ មានបញ្ហាក្នុងការដំណើរការ៖ លោកអ្នកអាចដាក់ API Key ខុស ឬអស់លុយពីគណនី OpenAI។ (លម្អិត៖ {e})")

    # =========================================================================
    # 📄 វគ្គទី ៥៖ បង្ហាញ និងទាញយកហ្វាល .SRT
    # =========================================================================
    if st.session_state.processing_done and uploaded_file:
        st.markdown("### 📄 លទ្ធផលទទួលបាន (Subtitle ខ្មែរ)")
        
        # បង្ហាញអត្ថបទដែលបានបកប្រែរួចពិតៗ
        st.text_area("មើលអត្ថបទគំរូជាមុន៖", value=st.session_state.final_srt, height=250)
        
        # ទាញយក
        st.download_button(
            label="📥 ទាញយកឯកសារ .SRT ទៅប្រើប្រាស់",
            data=st.session_state.final_srt,
            file_name=f"Khmer_Subtitle_{uploaded_file.name.split('.')[0]}.srt",
            mime="text/plain",
            use_container_width=True
        )

if __name__ == "__main__":
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = True
    if st.session_state.logged_in:
        run_subtitle_app()
