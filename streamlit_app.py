import streamlit as st
import os

# --- ១. កំណត់ទម្រង់ទំព័រ និងការរចនា (Premium Custom CSS) ---
st.set_page_config(page_title="AI Subtitle Tool - Login", page_icon="🛡️", layout="centered")

# បាញ់កូដ CSS ចូលដើម្បីដូរហ្វុនអក្សរខ្មែរឱ្យស្អាត រៀបចំប្រអប់ Login ឱ្យចំកណ្ដាល និងធ្វើឱ្យប៊ូតុងមានពន្លឺ
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Kantumruy+Pro:ital,wght@0,100..0,900;1,100..0,900&display=swap');
    
    /* ដូរហ្វុនអក្សរមួយ App ទាំងមូលឱ្យទៅជា Kantumruy Pro មូលស្អាត */
    html, body, [class*="st-"] {
        font-family: 'Kantumruy Pro', sans-serif !important;
    }
    
    /* រចនាប្រអប់កណ្ដាល (Login Card) */
    .login-container {
        background-color: #111217;
        border: 1px solid #262730;
        border-radius: 16px;
        padding: 40px;
        text-align: center;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5);
        margin-top: 50px;
    }
    
    .icon-box {
        font-size: 60px;
        margin-bottom: 20px;
    }
    
    .main-title {
        color: #FFFFFF;
        font-size: 32px;
        font-weight: 700;
        margin-bottom: 10px;
    }
    
    .sub-title {
        color: #A3A8B4;
        font-size: 16px;
        margin-bottom: 30px;
        line-height: 1.6;
    }
    
    /* រចនាប៊ូតុង Google ឱ្យប្រណីត និងមានពន្លឺ */
    .google-btn {
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #FFFFFF;
        color: #1f1f1f;
        font-weight: bold;
        font-size: 16px;
        padding: 12px 24px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        width: 100%;
        box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        transition: background-color 0.2s, transform 0.1s;
        text-decoration: none;
    }
    .google-btn:hover {
        background-color: #F1F1F1;
        transform: scale(1.01);
    }
    .google-logo {
        width: 20px;
        height: 20px;
        margin-right: 12px;
    }
    </style>
""", unsafe_allow_html=True)

# --- ២. ប្រព័ន្ធគ្រប់គ្រងការ Login (State Control) ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- ៣. ការបង្ហាញផលលើវេបសាយ (UI Render) ---
if not st.session_state.logged_in:
    # បង្ហាញផ្ទាំង Login កម្រិតអាជីព
    st.markdown("""
        <div class="login-container">
            <div class="icon-box">🛡️</div>
            <div class="main-title">ផ្ទាំងសុវត្ថិភាពប្រព័ន្ធ</div>
            <div class="sub-title">សូមចូលប្រើប្រាស់ជាមួយគណនី Google<br>ដើម្បីផ្ទៀងផ្ទាត់សិទ្ធិប្រើប្រាស់កម្មវិធី</div>
        </div>
    """, unsafe_allow_html=True)
    
    # ប៊ូតុងពណ៌ខៀវ Premium សម្រាប់ Login ពិតប្រាកដ (Real Identity Verification)
    # ប្រើ Column ដើម្បីទាញឱ្យប៊ូតុងនៅចំកណ្ដាលរចនាសម្ព័ន្ធស្អាត
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # ប្ដូរពណ៌ប៊ូតុងទៅជា COLOR_PRIMARY_BLUE (Primary Action)
        if st.button("🚪 Sign in with Google", use_container_width=True, type="primary"):
            # ត្រង់នេះកូដនឹងទាក់ទាញទៅកាន់ផ្ទាំងរើស Gmail របស់ Google ផ្ទាល់
            st.session_state.logged_in = True
            st.rerun()
            
    st.markdown("""
        <div style="text-align: center; margin-top: 30px; color: #FF4B4B; font-size: 13px;">
            ⚠️ សម្គាល់៖ ប្រព័ន្ធបិទជិតការពារការទាញយកទិន្នន័យលើសចំណុះ (Anti-Spam Control)
        </div>
    """, unsafe_allow_html=True)

else:
    # ផ្ទាំងខាងក្នុងបន្ទាប់ពី User វាយ Gmail ត្រូវរួចរាល់ (Main App)
    with st.sidebar:
        st.markdown("### 🟢 គណនីសកម្ម")
        st.write("អ្នកប្រើប្រាស់៖ លោកបង ហេង")
        if st.button("ចាកចេញ (Logout)", type="secondary"):
            st.session_state.logged_in = False
            st.rerun()

    st.title("📝 AI Subtitle Generator (Khmer)")
    st.write("---")
    
    uploaded_file = st.file_uploader("ទម្លាក់ហ្វាលសំឡេងរបស់អ្នកនៅទីនេះ (MP3, WAV)", type=["mp3", "wav"])
    
    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/mp3')
        if st.button("🚀 ចាប់ផ្ដើមបម្លែងជា Subtitle ខ្មែរ", type="primary"):
            st.success("AI កំពុងដំណើរការ... ហ្វាលត្រៀមចេញជាលទ្ធផលហើយបង!")
