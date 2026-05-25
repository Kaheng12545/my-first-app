import streamlit as st

def run_subtitle_app():
    # កូដទទេស្អាត រង់ចាំការបញ្ជាពីបង
    st.title("ទំព័រដើម (ចាប់ផ្តើមថ្មី)")
    st.success("🎉 ប្រព័ន្ធដំណើរការបានជោគជ័យ និងទទេស្អាតល្អ!")
    st.write("រង់ចាំការរៀបចំមុខងារថ្មី...")

if __name__ == "__main__":
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = True
    if st.session_state.logged_in:
        run_subtitle_app()
