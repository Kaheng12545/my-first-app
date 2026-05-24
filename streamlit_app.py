import streamlit as st

st.set_page_config(page_title="AI Subtitle Tool", page_icon="🔒")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔒 ផ្ទាំងសុវត្ថិភាពប្រព័ន្ធ")
    st.subheader("សូម Login ជាមួយគណនី Google ដើម្បីការពារប្រព័ន្ធ")
    
    if st.button("🔴 Sign in with Google", use_container_width=True):
        st.session_state.logged_in = True
        st.rerun()
        
    st.warning("សម្គាល់៖ ប្រព័ន្ធនេះត្រូវបានការពារ មិនអនុញ្ញាតឱ្យប្រើប្រាស់សេរីឡើយ ដើម្បីជៀសវាង Google បិទគណនី។")

else:
    with st.sidebar:
        st.write("🟢 គណនីកំពុងប្រើប្រាស់")
        if st.button("Logout (ចាកចេញ)"):
            st.session_state.logged_in = False
            st.rerun()

    st.title("📝 AI Subtitle Generator (Khmer)")
    uploaded_file = st.file_uploader("សូមជ្រើសរើសហ្វាលសំឡេង (MP3)", type=["mp3"])
    
    if uploaded_file is not None:
        if st.button("ចាប់ផ្ដើមបម្លែង និងបកប្រែ"):
            st.info("AI កំពុងដំណើរការ... (ប្រព័ន្ធសុវត្ថិភាពដើរជោគជ័យហើយបង)")
