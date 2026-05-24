import streamlit as st

# --- ១. កំណត់ទម្រង់ទំព័រ និងការរចនា (Custom Green Style) ---
st.set_page_config(page_title="AI Subtitle Tool - Login", page_icon="🛡️", layout="centered")

st.markdown("""
    <style>
    /* ទាញយកហ្វុនខ្មែរពី Google មកបង្កប់កុំឱ្យរឹងអក្សរ */
    @import url('https://fonts.googleapis.com/css2?family=Fasthand&family=Moul&family=Kantumruy+Pro&display=swap');

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
    
    /* រូបទី១៖ ចំណងជើងធំ ប្រើស្ទីលហ្វុន Khmer M1 (មិនឱ្យឌិតពេក ពណ៌បៃតងខ្ចី) */
    .main-title {
        font-family: 'Moul', 'Khmer OS Muol Light', sans-serif !important;
        color: #90EE90 !important; /* ពណ៌បៃតងខ្ចី Light Green */
        font-size: 30px;
        font-weight: normal !important; /* មិនឱ្យឌិតខ្លាំងពេក */
        margin-bottom: 25px;
        letter-spacing: 0.5px;
    }
    
    /* រូបទី២៖ អនុចំណងជើង ធ្វើឱ្យតូចជាងមុន និងប្រើហ្វុន Khmer Fasthand (ពណ៌បៃតងខ្ចី) */
    .sub-title {
        font-family: 'Fasthand', 'Khmer OS Fasthand', cursive, sans-serif !important;
        color: #A2E8A2 !important; /* ពណ៌បៃតងខ្ចីរាងស្រទន់ */
        font-size: 18px !important; /* កែឱ្យតូចជាងមុន */
        margin-bottom: 35px;
        line-height: 1.8;
    }
    
    /* រចនាប៊ូតុង Streamlit ឱ្យស្អាតសមរម្យ */
    div.stButton > button:first-child {
        background-color: #262730 !important; 
        color: #90EE90 !important; /* អក្សរលើប៊ូតុងពណ៌បៃតងខ្ចី */
        font-family: 'Kantumruy Pro', sans-serif !important;
        font-size: 16px !important;
        font-weight: bold !important;
        padding: 12px 24px !important;
        border-radius: 8px !important;
        border: 1px solid #444 !important;
        width: 100% !important;
        transition: all 0.2s ease !important;
    }
    div.stButton > button:first-child:hover {
        border-color: #90EE90 !important; /* លោតពន្លឺបៃតងពេលប៉ះម៉ៅស៍ */
        background-color: #1c1d24 !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- ២. ប្រព័ន្ធគ្រប់គ្រងការ Login (State Control) ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- ៣. ការបង្ហាញផលលើផ្ទាំងវេបសាយ (UI Render) ---
if not st.session_state.logged_in:
    # បង្ហាញ Card Login ជាមួយហ្វុន និងពណ៌បៃតងខ្ចីតាមបញ្ជាបង
    st.markdown("""
        <div class="login-container">
            <div style="font-size: 55px; margin-bottom: 15px;">🛡️</div>
            <div class="main-title">ផ្ទាំងសុវត្ថិភាពប្រព័ន្ធ</div>
            <div class="sub-title">សូមចូលប្រើប្រាស់ជាមួយគណនី Google<br>ដើម្បីផ្ទៀងផ្ទាត់សិទ្ធិប្រើប្រាស់កម្មវិធី</div>
        </div>
    """, unsafe_allow_html=True)
    
    # ប៊ូតុងដាក់រូបនាគ 🐉 លាយជាមួយរូប Google 🔴 នៅពីមុខតាមបំណងបង
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🐉🔴 Sign in with Google", use_container_width=True):
            st.session_state.logged_in = True
            st.rerun()
            
    st.markdown("""
        <div style="text-align: center; margin-top: 35px; color: #FF4B4B; font-size: 13px; font-family: 'Kantumruy Pro', sans-serif;">
            ⚠️ សម្គាល់៖ ប្រព័ន្ធបិទជិតការពារការទាញយកទិន្នន័យលើសចំណុះ (Anti-Spam Control)
        </div>
    """, unsafe_allow_html=True)

else:
    # ផ្ទាំងខាងក្នុងពេល Login ជោគជ័យ
    with st.sidebar:
        st.markdown("### 🟢 គណនីសកម្ម")
        st.write("អ្នកប្រើប្រាស់៖ លោកបង ហេង")
        if st.button("ចាកចេញ (Logout)"):
            st.session_state.logged_in = False
            st.rerun()

    st.title("📝 AI Subtitle Generator (Khmer)")
    st.write("---")
    uploaded_file = st.file_uploader("សូមជ្រើសរើសហ្វាលសំឡេងរបស់អ្នក (MP3)", type=["mp3"])
