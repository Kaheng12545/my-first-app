import streamlit as st

# --- ១. កំណត់ទម្រង់ទំព័រ និងការរចនា ---
st.set_page_config(page_title="AI Subtitle Tool - Login", page_icon="🛡️", layout="centered")

st.markdown("""
    <style>
    /* ទាញយកហ្វុនខ្មែរ */
    @import url('https://fonts.googleapis.com/css2?family=Khmer+OS+Muol+Light&family=Kantumruy+Pro&display=swap');

    /* ផ្ទៃខាងក្រោយពណ៌ខ្មៅ */
    .stApp {
        background-color: #0E1117; 
    }

    /* ប្រអប់កណ្ដាលពណ៌ខ្មៅ */
    .login-container {
        background-color: #0E1117; 
        padding: 20px; /* បន្ថយ padding ឱ្យខ្លីជាងមុន */
        text-align: center;
        max-width: 500px; 
        margin: 0 auto;
    }

    /* ឡូហ្គោ AI SEC */
    .logo-img {
        width: 120px; 
        margin-bottom: 10px; /* បន្ថយចន្លោះខាងក្រោមឡូហ្គោ */
    }

    /* ចំណងជើងធំ ហ្វុន Khmer M1 ពណ៌ស */
    .main-title {
        font-family: 'Khmer OS Muol Light', sans-serif !important;
        color: #FFFFFF !important; 
        font-size: 28px;
        margin-bottom: 15px;
    }

    /* អនុចំណងជើង ពណ៌ស ហ្វុន Kantumruy Pro */
    .sub-title {
        font-family: 'Kantumruy Pro', sans-serif !important;
        color: #FFFFFF !important; 
        font-size: 16px !important;
        margin-bottom: 15px; /* ទាញប៊ូតុងឱ្យរំកិលឡើងលើកៀកអក្សរ */
        line-height: 1.6;
    }

    /* ប៊ូតុង Google ពណ៌ស */
    div.stButton > button:first-child {
        background-color: #FFFFFF !important; 
        color: #3C4043 !important;
        font-family: 'Kantumruy Pro', sans-serif !important;
        font-size: 15px !important; 
        font-weight: 600 !important;
        padding: 8px 16px 8px 40px !important; 
        border-radius: 4px !important;
        border: 1px solid #DADCE0 !important;
        width: 100% !important; /* ដាក់ 100% ដើម្បីឱ្យវាពេញប្រអប់ Column កណ្ដាល */
        position: relative;
    }

    /* ឡូហ្គោ Google "G" ក្នុងប៊ូតុង */
    div.stButton > button:first-child::before {
        content: "";
        position: absolute;
        left: 15px; 
        top: 50%;
        transform: translateY(-50%);
        width: 18px; 
        height: 18px;
        background-image: url('https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg');
        background-size: contain;
        background-repeat: no-repeat;
    }

    /* អក្សរសម្គាល់ពណ៌ក្រហម ចំកណ្តាល */
    .warning-text {
        color: #FF4B4B; 
        font-size: 13px; 
        font-family: 'Kantumruy Pro', sans-serif;
        margin-top: 20px; /* ទាញអក្សរក្រហមឱ្យរំកិលឡើងលើកៀកប៊ូតុង */
        line-height: 1.6;
        text-align: center; 
    }
    </style>
""", unsafe_allow_html=True)

# --- ២. ប្រព័ន្ធគ្រប់គ្រងការ Login ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- ៣. ការបង្ហាញផលលើផ្ទាំងវេបសាយ ---
if not st.session_state.logged_in:
    st.markdown("""
        <div class="login-container">
            <img src="https://cdn-icons-png.flaticon.com/512/843/843296.png" class="logo-img" alt="AI SEC Logo">
            <div class="main-title">ផ្ទាំងសុវត្ថិភាពប្រព័ន្ធ</div>
            <div class="sub-title">សូមចូលប្រើប្រាស់ជាមួយគណនី Google<br>ដើម្បីផ្ទៀងផ្ទាត់សិទ្ធិប្រើប្រាស់កម្មវិធី</div>
        </div>
    """, unsafe_allow_html=True)
    
    # ប្រើ st.columns ដើម្បីចាក់សោរប៊ូតុងឱ្យនៅចំកណ្ដាល ១០០% លែងរត់ទៅឆ្វេងទៀតហើយ
    col1, col2, col3 = st.columns([1, 1.5, 1]) 
    with col2:
        if st.button("Sign in with Google", use_container_width=True):
            st.session_state.logged_in = True
            st.rerun()
            
    # អក្សរពណ៌ក្រហម
    st.markdown("""
        <div class="warning-text">
            សម្គាល់៖ សូមចូលប្រើប្រាស់គណនី Google ដើម្បីផ្ទៀងផ្ទាត់សិទ្ធិ<br>ប្រើប្រាស់កម្មវិធី។ សូមចូលប្រើប្រាស់ជាអនាមិក<br>ដើម្បីផ្ទៀងផ្ទាត់សិទ្ធិប្រើប្រាស់កម្មវិធី។
        </div>
    """, unsafe_allow_html=True)

else:
    with st.sidebar:
        st.markdown("### 🟢 គណនីសកម្ម")
        st.write("អ្នកប្រើប្រាស់៖ លោកបង ហេង")
        if st.button("ចាកចេញ (Logout)"):
            st.session_state.logged_in = False
            st.rerun()

    st.title("📝 AI Subtitle Generator (Khmer)")
    st.write("---")
    
    # ==================================================================
    # ⚠️ កុំភ្លេច Paste កូដចាស់ ១៤០ ជួររបស់បងនៅខាងក្រោមនេះ!
    # ==================================================================
