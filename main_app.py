import streamlit as st
import tempfile
import os
import time
from openai import OpenAI

def run_subtitle_app():
    # --- 🎨 តុបតែង UI ឱ្យស្អាត (លែងមានបញ្ហារញ៉េរញ៉ៃ) ---
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Khmer+OS+Muol+Light&family=Kantumruy+Pro:wght@300;400;500;700&display=swap');
    html, body, [class*="css"], [class*="st-"], p, span, div, label, li, button, input, select, textarea {
        font-family: 'Kantumruy Pro', sans-serif !important;
    }
    .main-title {
        text-align: center;
        color: #1E3A8A;
        font-family: 'Khmer OS Muol Light', sans-serif !important;
        font-size: 30px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="main-title">🎙️ កម្មវិធីបម្លែងសំឡេងទៅជា Subtitle ខ្មែរ (SRT) ពិតប្រាកដ</div>', unsafe_allow_html=True)

    # ==========================================
    # 🔑 ជំហានទី ១៖ ដាក់ API Key (ខានមិនបាន)
    # ==========================================
    st.markdown("### 🔑 ជំហានទី ១៖ បញ្ចូល OpenAI API Key")
    api_key = st.text_input("បញ្ចូល API Key របស់អ្នកទីនេះ (ចាប់ផ្តើមដោយ sk-...)", type="password")
    
    if not api_key:
        st.warning("⚠️ ប្រព័ន្ធត្រូវការ API Key ដើម្បីបញ្ជា AI ឱ្យធ្វើការស្តាប់ និងបកប្រែពិតប្រាកដ។")

    st.divider()

    # ==========================================
    # 📂 ជំហានទី ២៖ បញ្ចូលឯកសារសំឡេង
    # ==========================================
    st.markdown("### 📂 ជំហានទី ២៖ បញ្ចូលឯកសារសំឡេង (MP3, WAV, M4A)")
    uploaded_file = st.file_uploader("អូសឯកសារទម្លាក់ទីនេះ", type=['mp3', 'wav', 'm4a', 'mp4'])

    if uploaded_file:
        st.success(f"✅ ឯកសារបានត្រៀមរួចរាល់៖ {uploaded_file.name}")

    st.divider()

    # ==========================================
    # 🚀 ជំហានទី ៣៖ ដំណើរការម៉ាស៊ីន AI ពិតប្រាកដ
    # ==========================================
    st.markdown("### 🚀 ជំហានទី ៣៖ ចាប់ផ្តើមបម្លែងជាអក្សរខ្មែរ")
    
    if st.button("⚡ ចាប់ផ្តើមដំណើរការឥឡូវនេះ", type="primary", use_container_width=True):
        if not api_key:
            st.error("❌ សូមបញ្ចូល API Key នៅជំហានទី ១ សិន!")
        elif not uploaded_file:
            st.error("❌ សូមបញ្ចូលឯកសារសំឡេង នៅជំហានទី ២ សិន!")
        else:
            try:
                # ១. រៀបចំប្រព័ន្ធ
                client = OpenAI(api_key=api_key)
                progress_bar = st.progress(0)
                status_text = st.empty()

                # ២. រក្សាទុកហ្វាលជាបណ្តោះអាសន្ន ដើម្បីឱ្យ AI អាចអានបាន
                status_text.info("🔄 កំពុងរៀបចំឯកសារបញ្ជូនទៅកាន់ AI...")
                progress_bar.progress(10)
                
                with tempfile.NamedTemporaryFile(delete=False, suffix=f".{uploaded_file.name.split('.')[-1]}") as tmp_file:
                    tmp_file.write(uploaded_file.getvalue())
                    tmp_file_path = tmp_file.name

                # ៣. ប្រើ Whisper AI ដើម្បីស្តាប់ និងបញ្ចេញជាហ្វាល SRT ដើម (ភាសាអង់គ្លេស ឬដើម)
                status_text.info("🤖 AI កំពុងស្តាប់សំឡេង និងទាញយក Timestamps... (អាចចំណាយពេលបន្តិច)")
                progress_bar.progress(40)
                
                with open(tmp_file_path, "rb") as audio_file:
                    # បញ្ជាឱ្យ Whisper បញ្ចេញលទ្ធផលជា SRT ស្តង់ដារ
                    transcript_srt = client.audio.transcriptions.create(
                        model="whisper-1", 
                        file=audio_file, 
                        response_format="srt"
                    )
                
                # ៤. ប្រើ GPT-4o ដើម្បីបកប្រែអត្ថបទក្នុង SRT ទៅជាភាសាខ្មែរ ដោយរក្សា Timestamp ដដែល
                status_text.info("✨ កំពុងបកប្រែអត្ថបទទៅជាភាសាខ្មែរយ៉ាងរលូន...")
                progress_bar.progress(70)

                translation_prompt = """
                អ្នកគឺជាអ្នកបកប្រែ Subtitle ភាពយន្តដ៏ចំណាន។ 
                សូមបកប្រែអត្ថបទក្នុងឯកសារ SRT ខាងក្រោមនេះទៅជា **ភាសាខ្មែរ** ឱ្យបានត្រឹមត្រូវ និងពីរោះរលូន។
                លក្ខខណ្ឌដ៏តឹងរ៉ឹង៖ ហាមប៉ះពាល់ ឬផ្លាស់ប្តូរលេខលំដាប់ និង Timestamps (ឧទាហរណ៍៖ 00:00:01,000 --> 00:00:05,000) ជាដាច់ខាត។ បកប្រែតែអត្ថបទប៉ុណ្ណោះ។
                """

                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": translation_prompt},
                        {"role": "user", "content": transcript_srt}
                    ],
                    temperature=0.3 # កំណត់ឱ្យវាយកចិត្តទុកដាក់ខ្ពស់លើភាពត្រឹមត្រូវ
                )
                
                khmer_srt_content = response.choices[0].message.content

                # ៥. បញ្ចប់ការងារ និងលុបហ្វាលបណ្តោះអាសន្នចោល
                os.remove(tmp_file_path)
                progress_bar.progress(100)
                status_text.success("🎉 ដំណើរការចប់សព្វគ្រប់ ១០០%!")
                
                # រក្សាទុកលទ្ធផលក្នុង Session State
                st.session_state.final_srt = khmer_srt_content
                st.session_state.processing_done = True

            except Exception as e:
                st.error(f"❌ មានបញ្ហាក្នុងការដំណើរការ៖ {e}")

    # ==========================================
    # 📥 បង្ហាញលទ្ធផល និងទាញយកហ្វាល .SRT
    # ==========================================
    if getattr(st.session_state, 'processing_done', False):
        st.markdown("### 📄 លទ្ធផល Subtitle (ភាសាខ្មែរ)")
        st.text_area("មើលអត្ថបទគំរូជាមុន៖", value=st.session_state.final_srt, height=250)
        
        st.download_button(
            label="📥 ទាញយកឯកសារ .SRT ទៅប្រើប្រាស់",
            data=st.session_state.final_srt,
            file_name=f"Khmer_Subtitle_{uploaded_file.name.split('.')[0]}.srt",
            mime="text/plain",
            use_container_width=True
        )

if __name__ == "__main__":
    run_subtitle_app()
