import streamlit as st

# --- ១. កំណត់ទម្រង់ទំព័រ និងការរចនា (Dark Theme 100%) ---
st.set_page_config(page_title="AI Subtitle Tool - Login", page_icon="🛡️", layout="centered")

st.markdown("""
    <style>
    /* ទាញយកហ្វុនខ្មែរ */
    @import url('https://fonts.googleapis.com/css2?family=Fasthand&family=Moul&family=Kantumruy+Pro&display=swap');

    /* រចនាប្រអប់កណ្ដាលពណ៌ខ្មៅ (Dark Card) ដូចរូប ១០០% តែផ្ទៃខ្មៅ */
    .login-container {
        background-color: #111217; /* ផ្ទៃពណ៌ខ្មៅ/ប្រផេះងងឹត */
        border: 1px solid #262730; /* ស៊ុមប្រផេះ */
        border-radius: 16px;
        padding: 50px 40px;
        text-align: center;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.7); /* ស្រមោលក្រាស់ជាងមុនបន្តិច */
        margin-top: 20px;
        max-width: 550px; 
        margin-left: auto;
        margin-right: auto;
    }
    
    /* ឡូហ្គោ AI SEC ធំ */
    .logo-img {
        width: 140px; 
        margin-bottom: 25px;
    }

    /* ចំណងជើងធំ ហ្វុន Khmer M1 ពណ៌ស */
    .main-title {
        font-family: 'Moul', 'Khmer OS Muol Light', sans-serif !important;
        color: #FFFFFF !important; /* ប្ដូរទៅពណ៌ស ដើម្បីលេចលើផ្ទៃខ្មៅ */
        font-size: 32px;
        font-weight: normal !important;
        margin-bottom: 20px;
        line-height: 1.6;
    }
    
    /* អនុចំណងជើង ហ្វុន Khmer Fasthand ពណ៌ប្រផេះស្រាល */
    .sub-title {
        font-family: 'Fasthand', 'Khmer OS Fasthand', cursive, sans-serif !important;
        color: #B0B0B0 !important; /* ប្ដូរទៅពណ៌ប្រផេះស្រាល */
        font-size: 22px !important;
        margin-bottom: 35px;
        line-height: 1.8;
    }
    
    /* រចនាប៊ូតុង Streamlit ឱ្យដូចប៊ូតុង Google ផ្លូវការ (ពណ៌ស តូចជាងមុន ២០%) */
    div.stButton > button:first-child {
        background-color: #FFFFFF !important; 
        color: #3C4043 !important;
        font-family: 'Kantumruy Pro', sans-serif !important;
        font-size: 15px !important; /* ធ្វើឱ្យអក្សរតូចជាងមុនបន្តិច */
        font-weight: 600 !important;
        padding: 8px 24px 8px 40px !important; /* បង្រួមទំហំប៊ូតុង និងទុកកន្លែងដាក់ឡូហ្គោ */
        border-radius: 4px !important;
        border: 1px solid #DADCE0 !important;
        width: 80% !important; /* បង្រួមប្រវែងប៊ូតុង ២០% */
        margin: 0 auto; /* ទាញប៊ូតុងឱ្យនៅចំកណ្ដាល */
        display: block;
        position: relative;
        box-shadow: 0 1px 2px 0 rgba(0,0,0,0.3) !important;
        transition: background-color 0.2s, box-shadow 0.2s !important;
    }
    
    /* បង្កប់រូប Logo "G" ចូលក្នុងប៊ូតុង (រុញឱ្យកៀកអក្សរ) */
    div.stButton > button:first-child::before {
        content: "";
        position: absolute;
        left: 20px; /* រុញឡូហ្គោឱ្យកៀកអក្សរបន្តិច */
        top: 50%;
        transform: translateY(-50%);
        width: 18px; /* ឡូហ្គោតូចជាងមុនបន្តិចឱ្យសមនឹងប៊ូតុង */
        height: 18px;
        background-image: url('https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg');
        background-size: contain;
        background-repeat: no-repeat;
    }

    div.stButton > button:first-child:hover {
        background-color: #F8F9FA !important;
        box-shadow: 0 1px 3px 1px rgba(0,0,0,0.15) !important;
    }

    /* អក្សរសម្គាល់ពណ៌ក្រហមខាងក្រោម */
    .warning-text {
        color: #FF4B4B; 
        font-size: 14px; 
        font-family: 'Kantumruy Pro', sans-serif;
        margin-top: 35px;
        line-height: 1.6;
    }
    </style>
""", unsafe_allow_html=True)

# --- ២. ប្រព័ន្ធគ្រប់គ្រងការ Login (State Control) ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- ៣. ការបង្ហាញផលលើផ្ទាំងវេបសាយ (UI Render) ---
if not st.session_state.logged_in:
    # ផ្ទាំង HTML បង្ហាញ Card ពណ៌ខ្មៅ និងឡូហ្គោធំ
    st.markdown("""
        <div class="login-container">
            <img src="https://cdn-icons-png.flaticon.com/512/843/843296.png" class="logo-img" alt="AI SEC Logo">
            <div class="main-title">ផ្ទាំងសុវត្ថិភាពប្រព័ន្ធ</div>
            <div class="sub-title">សូមចូលប្រើប្រាស់ជាមួយគណនី Google<br>ដើម្បីផ្ទៀងផ្ទាត់សិទ្ធិប្រើប្រាស់កម្មវិធី</div>
            <br>
    """, unsafe_allow_html=True)
    
    # ប៊ូតុងត្រូវបានទាញឱ្យនៅកណ្ដាលរួចហើយដោយ CSS (width: 80%, margin: 0 auto)
    if st.button("Sign in with Google", use_container_width=True):
        st.session_state.logged_in = True
        st.rerun()
            
    st.markdown("""
            <div class="warning-text">
                ⚠️ សម្គាល់៖ សូមចូលប្រើប្រាស់គណនី Google ដើម្បីផ្ទៀងផ្ទាត់សិទ្ធិ<br>ប្រើប្រាស់កម្មវិធី។ សូមចូលប្រើប្រាស់ជាអនាមិក<br>ដើម្បីផ្ទៀងផ្ទាត់សិទ្ធិប្រើប្រាស់កម្មវិធី។
            </div>
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
    # ⚠️ Paste កូដចាស់ ១៤0 ជួររបស់បងនៅខាងក្រោមនេះ!
    # ==================================================================
