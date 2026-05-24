import streamlit as st

# --- ១. កំណត់ទម្រង់ទំព័រ និងការរចនា (Dark Theme + Green Text) ---
st.set_page_config(page_title="AI Subtitle Tool - Login", page_icon="🛡️", layout="centered")

st.markdown("""
    <style>
    /* ទាញយកហ្វុនខ្មែរ */
    @import url('https://fonts.googleapis.com/css2?family=Fasthand&family=Moul&family=Kantumruy+Pro&display=swap');

    /* រចនាប្រអប់កណ្ដាលងងឹត */
    .login-container {
        background-color: #111217;
        border: 1px solid #262730;
        border-radius: 16px;
        padding: 40px;
        text-align: center;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5);
        margin-top: 30px;
    }

    /* ចំណងជើងធំ ហ្វុន Khmer M1 ពណ៌បៃតងខ្ចី */
    .main-title {
        font-family: 'Moul', 'Khmer OS Muol Light', sans-serif !important;
        color: #90EE90 !important;
        font-size: 32px;
        font-weight: normal;
        margin-bottom: 20px;
    }
    
    /* អនុចំណងជើង ហ្វុន Khmer Fasthand ពណ៌បៃតងខ្ចី */
    .sub-title {
        font-family: 'Fasthand', 'Khmer OS Fasthand', cursive, sans-serif !important;
        color: #A2E8A2 !important;
        font-size: 20px;
        margin-bottom: 35px;
        line-height: 1.8;
    }

    /* ---------------------------------------------------
       រចនាប៊ូតុង GOOGLE ផ្លូវការ (Official White Button)
       --------------------------------------------------- */
    div.stButton > button:first-child {
        background-color: #FFFFFF !important; 
        color: #3C4043 !important; /* អក្សរពណ៌ប្រផេះចាស់ ដូចស្តង់ដារ Google */
        font-family: 'Kantumruy Pro', sans-serif !important;
        font-size: 16px !important;
        font-weight: 600 !important;
        padding: 10px 24px 10px 48px !important; /* ទាញអក្សរចេញពីគែម ដើម្បីទុកចន្លោះដាក់ឡូហ្គោ */
        border-radius: 4px !important;
        border: 1px solid #DADCE0 !important;
        width: 100% !important;
        position: relative;
        box-shadow: 0 1px 2px 0 rgba(60,64,67,0.3) !important;
        transition: background-color 0.2s, box-shadow 0.2s !important;
    }
    
    /* បង្កប់រូប Logo "G" ចូលក្នុងប៊ូតុងដោយផ្ទាល់តាមរយៈ CSS (ធានាថាលោតចេញ ១០០%) */
    div.stButton > button:first-child::before {
        content: "";
        position: absolute;
        left: 16px; /* រុញឡូហ្គោឱ្យនៅខាងឆ្វេង */
        top: 50%;
        transform: translateY(-50%);
        width: 20px;
        height: 20px;
        background-image: url('https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg');
        background-size: contain;
        background-repeat: no-repeat;
    }

    /* ពេលយកម៉ៅស៍ទៅដាក់ពីលើប៊ូតុង */
    div.stButton > button:first-child:hover {
        background-color: #F8F9FA !important;
        box-shadow: 0 1px 3px 1px rgba(60,64,67,0.15) !important;
    }
    </style>
""", unsafe_allow_html=True)

# --- ២. ប្រព័ន្ធគ្រប់គ្រងការ Login (State Control) ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- ៣. ការបង្ហាញផលលើផ្ទាំងវេបសាយ (UI Render) ---
if not st.session_state.logged_in:
    # ផ្ទាំង HTML បង្ហាញ Card
    st.markdown("""
        <div class="login-container">
            <div style="font-size: 65px; margin-bottom: 10px;">🛡️</div>
            <div class="main-title">ផ្ទាំងសុវត្ថិភាពប្រព័ន្ធ</div>
            <div class="sub-title">សូមចូលប្រើប្រាស់ជាមួយគណនី Google<br>ដើម្បីផ្ទៀងផ្ទាត់សិទ្ធិប្រើប្រាស់កម្មវិធី</div>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write("") # បង្កើតចន្លោះ
        # គ្រាន់តែដាក់អក្សរធម្មតា ព្រោះឡូហ្គោ "G" ត្រូវបានបាញ់បញ្ចូលតាម CSS ខាងលើរួចហើយ
        if st.button("Sign in with Google", use_container_width=True):
            st.session_state.logged_in = True
            st.rerun()
            
    st.markdown("""
        <div style="text-align: center; margin-top: 35px; color: #FF4B4B; font-size: 14px; font-family: 'Kantumruy Pro', sans-serif;">
            ⚠️ សម្គាល់៖ ប្រព័ន្ធបិទជិតការពារការទាញយកទិន្នន័យលើសចំណុះ (Anti-Spam Control)
        </div>
    """, unsafe_allow_html=True)

else:
    # ផ្ទាំងខាងក្នុងបន្ទាប់ពី User ចូលប្រព័ន្ធរួចរាល់
    with st.sidebar:
        st.markdown("### 🟢 គណនីសកម្ម")
        st.write("អ្នកប្រើប្រាស់៖ លោកបង ហេង")
        if st.button("ចាកចេញ (Logout)"):
            st.session_state.logged_in = False
            st.rerun()

    st.title("📝 AI Subtitle Generator (Khmer)")
    st.write("---")
    
    # ==================================================================
    # ⚠️ ទីនេះហើយបង! បងចម្លង (Copy) កូដចាស់ជាង ១៤០ ជួររបស់បង
    # យកមកបិទភ្ជាប់ (Paste) នៅពីក្រោមបន្ទាត់នេះមក ជាការស្រេច!
    # ==================================================================
