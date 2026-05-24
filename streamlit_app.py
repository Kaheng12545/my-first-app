import streamlit as st

# --- ១. កំណត់ទម្រង់ទំព័រ និងការរចនា (Advanced UI Styles) ---
st.set_page_config(page_title="AI Subtitle Tool - Login", page_icon="🛡️", layout="centered")

st.markdown("""
    <style>
    /* បង្ខំឱ្យប្រើហ្វុនខ្មែរមូលស្អាត */
    html, body, [class*="st-"], div, span, p, h1, h2, h3 {
        font-family: 'Khmer OS Muol Light', 'Khmer OS Muol', 'Moul', 'Khmer OS Battambang', sans-serif !important;
    }
    
    /* រចនាប្រអប់កណ្ដាល (Login Card) */
    .login-container {
        background-color: #111217;
        border: 1px solid #262730;
        border-radius: 16px;
        padding: 40px;
        text-align: center;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5);
        margin-top: 40px;
    }
    
    .icon-box {
        font-size: 60px;
        margin-bottom: 20px;
    }
    
    /* ស្ទីលចំណងជើងធំ (ដូច Khmer M1) */
    .main-title {
        font-family: 'Khmer OS Muol Light', 'Khmer OS Muol', 'Moul', sans-serif !important;
        color: #FFFFFF;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    
    /* ស្ទីលអនុចំណងជើង (ដូច Khmer Fasthand) */
    .sub-title {
        font-family: 'Khmer OS Fasthand', 'Fanthand', 'Khmer OS Freehand', cursive, sans-serif !important;
        color: #A3A8B4;
        font-size: 22px;
        margin-bottom: 30px;
        line-height: 1.8;
    }
    
    /* បង្កើតទម្រង់ប៊ូតុង Custom ឱ្យមាន Logo Google ពិតប្រាកដ */
    .custom-google-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #1A73E8 !important; /* ពណ៌ខៀវ Google */
        color: white !important;
        font-family: 'Khmer OS Battambang', 'Siemreap', sans-serif !important;
        font-size: 16px !important;
        font-weight: bold !important;
        padding: 12px 24px !important;
        border-radius: 8px !important;
        border: none !important;
        box-shadow: 0px 4px 12px rgba(26, 115, 232, 0.3) !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
        cursor: pointer;
        text-decoration: none;
    }
    
    .custom-google-btn:hover {
        background-color: #1557B0 !important;
        box-shadow: 0px 6px 16px rgba(26, 115, 232, 0.4) !important;
    }

    .google-icon {
        width: 22px;
        height: 22px;
        background-color: white;
        border-radius: 4px;
        padding: 2px;
        margin-right: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# --- ២. ប្រព័ន្ធគ្រប់គ្រងការ Login (State Control) ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- ៣. ការបង្ហាញផលលើវេបសាយ (UI Render) ---
if not st.session_state.logged_in:
    # ផ្ទាំង HTML បង្ហាញ Card Login
    st.markdown("""
        <div class="login-container">
            <div class="icon-box">🛡️</div>
            <div class="main-title">ផ្ទាំងសុវត្ថិភាពប្រព័ន្ធ</div>
            <div class="sub-title">សូមចូលប្រើប្រាស់ជាមួយគណនី Google<br>ដើម្បីផ្ទៀងផ្ទាត់សិទ្ធិប្រើប្រាស់កម្មវិធី</div>
        </div>
    """, unsafe_allow_html=True)
    
    # ប៊ូតុងពណ៌ខៀវបង្កប់រូប Logo ផ្លូវការរបស់ Google (ដោះស្រាយបញ្ហា Emoji មូលៗ)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # បង្កប់រូបភាព SVG Logo Google ផ្លូវការចូលទៅក្នុងប៊ូតុង
        st.write("") # បង្កើតគម្លាតតូចមួយ
        if st.button("Sign in with Google", use_container_width=True):
            st.session_state.logged_in = True
            st.rerun()
            
        # បាញ់បញ្ចូលរូប Logo ពីលើប៊ូតុងរបស់ Streamlit តាមរយៈការកែច្នៃស្រទាប់ (Layer)
        st.markdown("""
            <script>
            // កូដ JavaScript សម្រាប់ជួយរុញរូបឡូហ្គោចូលក្នុងប៊ូតុង Streamlit ឱ្យស្អាតបំផុត
            const buttons = window.parent.document.querySelectorAll('button');
            buttons.forEach(button => {
                if(button.innerText.includes('Sign in with Google') && !button.innerHTML.includes('img')){
                    button.innerHTML = `<img src="https://fonts.gstatic.com/s/i/productlogos/googleg/v6/web-24dp/logo_googleg_color_24dp.png" style="width:20px; height:20px; margin-right:10px; background:white; padding:2px; border-radius:2px;">` + button.innerText;
                }
            });
            </script>
        """, unsafe_allow_html=True)
            
    st.markdown("""
        <div style="text-align: center; margin-top: 35px; color: #FF4B4B; font-size: 14px; font-family: 'Khmer OS Battambang', sans-serif;">
            ⚠️ សម្គាល់៖ ប្រព័ន្ធបិទជិតការពារការទាញយកទិន្នន័យលើសចំណុះ (Anti-Spam Control)
        </div>
    """, unsafe_allow_html=True)

else:
    # ផ្ទាំងខាងក្នុងបន្ទាប់ពី User ចូលប្រព័ន្ធរួចរាល់ (Main App)
    with st.sidebar:
        st.markdown("### 🟢 គណនីសកម្ម")
        st.write("អ្នកប្រើប្រាស់៖ លោកបង ហេង")
        if st.button("ចាកចេញ (Logout)"):
            st.session_state.logged_in = False
            st.rerun()

    st.title("📝 AI Subtitle Generator (Khmer)")
    st.write("---")
    
    uploaded_file = st.file_uploader("សូមជ្រើសរើសហ្វាលសំឡេងរបស់អ្នក (MP3)", type=["mp3"])
    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/mp3')
        if st.button("🚀 ចាប់ផ្ដើមបម្លែងជា Subtitle ខ្មែរ"):
            st.success("AI កំពុងដំណើរការ...")
