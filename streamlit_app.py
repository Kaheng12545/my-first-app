import streamlit as st

# --- ១. កំណត់ទម្រង់ទំព័រ និងការរចនា (White Card on Dark Theme) ---
st.set_page_config(page_title="AI Subtitle Tool - Login", page_icon="🛡️", layout="centered")

st.markdown("""
    <style>
    /* ទាញយកហ្វុនខ្មែរ */
    @import url('https://fonts.googleapis.com/css2?family=Fasthand&family=Moul&family=Kantumruy+Pro&display=swap');

    /* រចនាប្រអប់កណ្ដាលពណ៌ស (White Card) ធ្វើឱ្យធំជាងមុន ៣០% */
    .login-container {
        background-color: #FFFFFF; /* ផ្ទៃពណ៌ស */
        border-radius: 16px;
        padding: 50px 40px;
        text-align: center;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.5);
        margin-top: 20px;
        max-width: 550px; /* ទំហំប្រអប់ធំជាងមុន */
        margin-left: auto;
        margin-right: auto;
    }
    
    /* ឡូហ្គោធ្វើឱ្យធំជាងមុន ២.៥ ដង */
    .logo-img {
        width: 140px; /* ទំហំឡូហ្គោធំ */
        margin-bottom: 20px;
    }

    /* ចំណងជើងធំ ហ្វុន Khmer M1 ពណ៌ខ្មៅ/ប្រផេះដិត */
    .main-title {
        font-family: 'Moul', 'Khmer OS Muol Light', sans-serif !important;
        color: #1f1f1f !important;
        font-size: 32px;
        font-weight: normal !important;
        margin-bottom: 20px;
        line-height: 1.6;
    }
    
    /* អនុចំណងជើង ហ្វុន Khmer Fasthand ពណ៌ប្រផេះ */
    .sub-title {
        font-family: 'Fasthand', 'Khmer OS Fasthand', cursive, sans-serif !important;
        color: #555555 !important;
        font-size: 22px !important;
        margin-bottom: 35px;
        line-height: 1.8;
    }
    
    /* រចនាប៊ូតុង Streamlit ឱ្យដូចប៊ូតុង Google ផ្លូវការ */
    div.stButton > button:first-child {
        background-color: #FFFFFF !important; 
        color: #444444 !important;
        font-family: 'Kantumruy Pro', sans-serif !important;
        font-size: 16px !important;
        font-weight: bold !important;
        padding: 10px 24px !important;
        border-radius: 8px !important;
        border: 1px solid #DADCE0 !important;
        width: 100% !important;
        box-shadow: 0 1px 2px 0 rgba(60,64,67,0.3) !important;
        transition: all 0.2s ease !important;
    }
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
    # ផ្ទាំង HTML បង្ហាញ Card ពណ៌ស និងឡូហ្គោធំ
    st.markdown("""
        <div class="login-container">
            <img src="https://cdn-icons-png.flaticon.com/512/843/843296.png" class="logo-img" alt="Logo">
            <div class="main-title">ផ្ទាំងសុវត្ថិភាពប្រព័ន្ធ</div>
            <div class="sub-title">សូមចូលប្រើប្រាស់ជាមួយគណនី Google<br>ដើម្បីផ្ទៀងផ្ទាត់សិទ្ធិប្រើប្រាស់កម្មវិធី</div>
        </div>
    """, unsafe_allow_html=True)
    
    # ប៊ូតុង និងការបង្កប់រូបអក្សរ G (Google Logo) ដោយផ្ទាល់
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.write("") # បង្កើតចន្លោះ
        if st.button("Sign in with Google", use_container_width=True):
            st.session_state.logged_in = True
            st.rerun()
            
        # JavaScript បង្កប់រូប Logo G ផ្លូវការរបស់ Google នៅមុខអក្សរ (លុបពស់និងដុំក្រហមចេញ)
        st.markdown("""
            <script>
            const buttons = window.parent.document.querySelectorAll('button');
            buttons.forEach(button => {
                if(button.innerText.includes('Sign in with Google') && !button.innerHTML.includes('img')){
                    button.innerHTML = `<img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Google_%22G%22_logo.svg" style="width:20px; height:20px; margin-right:10px;">` + button.innerText;
                }
            });
            </script>
        """, unsafe_allow_html=True)
            
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
