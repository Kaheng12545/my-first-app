import streamlit as st

# --- ១. កំណត់ទម្រង់ទំព័រ និងការរចនា (Advanced UI Styles) ---
st.set_page_config(page_title="AI Subtitle Tool - Login", page_icon="🛡️", layout="centered")

# ប្រើប្រាស់ CSS បង្ខំ Font ក្នុងម៉ាស៊ីនឱ្យដើរភ្លាមៗ និងរចនាប៊ូតុងខៀវ
st.markdown("""
    <style>
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
    
    /* រូបទី១៖ បង្ខំឱ្យចេញហ្វុនស្ទីលខ្មែរមូលដិត (ដូច Khmer M1) */
    .main-title {
        font-family: 'Khmer OS Muol Light', 'Khmer OS Muol', 'Moul', 'Khmer OS Battambang', sans-serif !important;
        color: #FFFFFF;
        font-size: 32px;
        font-weight: bold;
        margin-bottom: 20px;
        letter-spacing: 1px;
    }
    
    /* រូបទី២៖ បង្ខំឱ្យចេញហ្វុនស្ទីលអក្សរដៃ/ឆ្លាក់ (ដូច Khmer Fasthand) */
    .sub-title {
        font-family: 'Khmer OS Fasthand', 'Fanthand', 'Khmer OS Freehand', 'Khmer OS Battambang', cursive, sans-serif !important;
        color: #A3A8B4;
        font-size: 20px;
        margin-bottom: 30px;
        line-height: 1.8;
    }
    
    /* រូបទី៣៖ បង្ខំកូដប៊ូតុងឱ្យទៅជាពណ៌ខៀវប្រណីត និងប្រើហ្វុនមូលស្អាត */
    div.stButton > button:first-child {
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
    }
    
    /* ពេលយកម៉ៅស៍ទៅដាក់ពីលើប៊ូតុង */
    div.stButton > button:first-child:hover {
        background-color: #1557B0 !important;
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
    # បង្ហាញផ្ទាំង Login តាមទម្រង់ HTML ដើម្បីឱ្យហ្វុនដើរត្រឹមត្រូវ
    st.markdown("""
        <div class="login-container">
            <div class="icon-box">🛡️</div>
            <div class="main-title">ផ្ទាំងសុវត្ថិភាពប្រព័ន្ធ</div>
            <div class="sub-title">សូមចូលប្រើប្រាស់ជាមួយគណនី Google<br>ដើម្បីផ្ទៀងផ្ទាត់សិទ្ធិប្រើប្រាស់កម្មវិធី</div>
        </div>
    """, unsafe_allow_html=True)
    
    # ទីតាំងប៊ូតុងពណ៌ខៀវ និងដាក់ម៉ាកសញ្ញា Google Emoji (🔴🔵🟡🟢)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔴🔵🟡🟢 Sign in with Google", use_container_width=True):
            st.session_state.logged_in = True
            st.rerun()
            
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
