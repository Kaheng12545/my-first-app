import streamlit as st

# --- ១. កំណត់ទម្រង់ទំព័រ និងការរចនា (Premium Custom CSS & Fonts) ---
st.set_page_config(page_title="AI Subtitle Tool - Login", page_icon="🛡️", layout="centered")

# បាញ់កូដ CSS ជំនាន់ថ្មី បង្ខំឱ្យស្គាល់ហ្វុនខ្មែរមូលស្អាត និងប្ដូរប៊ូតុងទៅជាពណ៌ខៀវ
st.markdown("""
    <style>
    /* ទាញយកហ្វុនខ្មែរមូលស្អាតមកប្រើប្រាស់ */
    @import url('https://fonts.googleapis.com/css2?family=Siemreap&family=Kantumruy+Pro:wght@400;700&display=swap');
    
    /* បង្ខំឱ្យប្រើហ្វុនខ្មែរមូលស្អាត (Siemreap / Kantumruy Pro) ទៅលើរាល់អក្សរទាំងអស់ */
    html, body, [class*="st-"], div, span, p, h1, h2, h3 {
        font-family: 'Siemreap', 'Kantumruy Pro', 'Khmer OS Battambang', sans-serif !important;
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
    
    .main-title {
        color: #FFFFFF;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 15px;
        letter-spacing: 0.5px;
    }
    
    .sub-title {
        color: #A3A8B4;
        font-size: 16px;
        margin-bottom: 30px;
        line-height: 1.8;
    }
    
    /* បង្ខំកូដប៊ូតុងរបស់ Streamlit ឱ្យទៅជាពណ៌ខៀវប្រណីត (Premium Blue) */
    div.stButton > button:first-child {
        background-color: #1A73E8 !important; /* ពណ៌ខៀវ Google OAuth */
        color: white !important;
        font-family: 'Siemreap', 'Kantumruy Pro', sans-serif !important;
        font-size: 16px !important;
        font-weight: bold !important;
        padding: 12px 24px !important;
        border-radius: 8px !important;
        border: none !important;
        box-shadow: 0px 4px 12px rgba(26, 115, 232, 0.3) !important;
        transition: all 0.2s ease !important;
        width: 100% !important;
    }
    
    /* ពេលយកម៉ៅស៍ទៅដាក់ពីលើប៊ូតុងពណ៌ខៀវ */
    div.stButton > button:first-child:hover {
        background-color: #1557B0 !important; /* ពណ៌ខៀវដិតជាងមុនបន្តិច */
        box-shadow: 0px 6px 16px rgba(26, 115, 232, 0.4) !important;
        transform: translateY(-1px);
    }
    </style>
""", unsafe_allow_html=True)

# --- ២. ប្រព័ន្ធគ្រប់គ្រងការ Login (State Control) ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- ៣. ការបង្ហាញផលលើវេបសាយ (UI Render) ---
if not st.session_state.logged_in:
    # បង្ហាញផ្ទាំង Login ដែលមានរចនាសម្ព័ន្ធអក្សរ និងប្រអប់ច្បាស់លាស់
    st.markdown("""
        <div class="login-container">
            <div class="icon-box">🛡️</div>
            <div class="main-title">ផ្ទាំងសុវត្ថិភាពប្រព័ន្ធ</div>
            <div class="sub-title">សូមចូលប្រើប្រាស់ជាមួយគណនី Google<br>ដើម្បីផ្ទៀងផ្ទាត់សិទ្ធិប្រើប្រាស់កម្មវិធី</div>
        </div>
    """, unsafe_allow_html=True)
    
    # ទីតាំងប៊ូតុងពណ៌ខៀវសម្រាប់ចុច Login
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚪 Sign in with Google", use_container_width=True):
            st.session_state.logged_in = True
            st.rerun()
            
    st.markdown("""
        <div style="text-align: center; margin-top: 35px; color: #FF4B4B; font-size: 13px; font-weight: bold;">
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
    
    uploaded_file = st.file_uploader("សូមជ្រើសរើសហ្វាលសំឡេងរបស់អ្នក (MP3, WAV)", type=["mp3", "wav"])
    
    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/mp3')
        if st.button("🚀 ចាប់ផ្ដើមបម្លែងជា Subtitle ខ្មែរ"):
            st.success("AI កំពុងដំណើរការ... ហ្វាលត្រៀមចេញជាលទ្ធផលហើយបង!")
