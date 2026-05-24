import streamlit as st

# --- ១. កំណត់ទម្រង់ទំព័រ និងការរចនា (White Theme) ---
st.set_page_config(page_title="AI Subtitle Tool - Login", page_icon="🛡️", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Khmer+OS+Muol+Light&family=Kantumruy+Pro&display=swap');

.stApp { background-color: #F8F9FA; }
.login-container {
    background-color: #FFFFFF;
    border: 1px solid #E0E0E0;
    border-radius: 12px;
    padding: 40px;
    text-align: center;
    max-width: 550px;
    margin: 0 auto;
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.05);
}
.logo-img { width: 140px; margin-bottom: 20px; }
.main-title {
    font-family: 'Khmer OS Muol Light', sans-serif !important;
    color: #202124 !important; 
    font-size: 32px;
    margin-bottom: 15px;
}
.sub-title {
    font-family: 'Kantumruy Pro', sans-serif !important;
    color: #5F6368 !important;
    font-size: 18px !important;
    margin-bottom: 35px;
    line-height: 1.6;
}
.google-btn {
    text-decoration: none !important;
    display: block;
    background-color: #FFFFFF;
    color: #3C4043;
    font-family: 'Kantumruy Pro', sans-serif;
    font-size: 15px;
    font-weight: 600;
    padding: 10px 16px 10px 40px;
    border-radius: 4px;
    border: 1px solid #DADCE0;
    width: 250px;
    margin: 0 auto;
    position: relative;
    text-align: center;
    box-shadow: 0 1px 2px 0 rgba(0,0,0,0.1);
    transition: background-color 0.2s;
}
.google-btn:hover { background-color: #F8F9FA; }
.google-btn::before {
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
.warning-text {
    color: #D93025;
    font-size: 14px;
    font-family: 'Kantumruy Pro', sans-serif;
    margin-top: 35px;
    line-height: 1.6;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# --- ២. ប្រព័ន្ធគ្រប់គ្រងការ Login ពិតប្រាកដជាមួយ Google ---
CLIENT_ID = "23291298297-f4h36r7vnktqt26m4io96512slrduv8l.apps.googleusercontent.com"
REDIRECT_URI = "https://kaheng12545-my-first-app-streamlit-app-b5z6u0.streamlit.app"

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

query_params = st.query_params
if "code" in query_params:
    st.session_state.logged_in = True
    st.query_params.clear()

# --- ៣. ការបង្ហាញផលលើផ្ទាំងវេបសាយ ---
if not st.session_state.logged_in:
    auth_url = f"https://accounts.google.com/o/oauth2/v2/auth?client_id={CLIENT_ID}&response_type=code&scope=openid%20email%20profile&redirect_uri={REDIRECT_URI}"

    # ជួសជុល៖ ដកគម្លាត (Spaces) ចេញទាំងអស់ដើម្បីកុំឱ្យវាចេញជាកូដខ្មៅៗទៀត
    html_code = f"""
<div class="login-container">
<img src="https://cdn-icons-png.flaticon.com/512/843/843296.png" class="logo-img" alt="AI SEC Logo">
<div class="main-title">ផ្ទាំងសុវត្ថិភាពប្រព័ន្ធ</div>
<div class="sub-title">សូមចូលប្រើប្រាស់ជាមួយគណនី Google<br>ដើម្បីផ្ទៀងផ្ទាត់សិទ្ធិប្រើប្រាស់កម្មវិធី</div>
<a href="{auth_url}" class="google-btn">Sign in with Google</a>
<div class="warning-text">សម្គាល់៖ សូមចូលប្រើប្រាស់គណនី Google ដើម្បីផ្ទៀងផ្ទាត់សិទ្ធិ<br>ប្រើប្រាស់កម្មវិធី។ សូមចូលប្រើប្រាស់ជាអនាមិក<br>ដើម្បីផ្ទៀងផ្ទាត់សិទ្ធិប្រើប្រាស់កម្មវិធី។</div>
</div>
"""
    st.markdown(html_code, unsafe_allow_html=True)

else:
    with st.sidebar:
        st.markdown("### 🟢 គណនីសកម្ម")
        st.write("ស្ថានភាព៖ បានផ្ទៀងផ្ទាត់ជោគជ័យ")
        if st.button("ចាកចេញ (Logout)"):
            st.session_state.logged_in = False
            st.rerun()

    st.title("📝 AI Subtitle Generator (Khmer)")
    st.write("---")
    
    # ==================================================================
    # ⚠️ យកកូដ AI ចាស់ ១៤០ ជួររបស់បងមក Paste បន្តនៅខាងក្រោមនេះ
    # ==================================================================
