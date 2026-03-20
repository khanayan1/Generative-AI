import streamlit as st
import time

# Page config
st.set_page_config(page_title="Sorry ❤️", page_icon="💔")

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = 1

# -------- PAGE 1 --------
if st.session_state.page == 1:
    st.markdown(
        """
        <h1 style='text-align: center; color: red; font-size: 80px;'>
        SORRY 💔
        </h1>
        <h3 style='text-align: center;'>I really didn't mean to hurt you...</h3>
        """,
        unsafe_allow_html=True
    )

    st.write("\n")
    
    if st.button("Click if you still care ❤️"):
        with st.spinner("Opening my heart..."):
            time.sleep(2)
        st.session_state.page = 2
        st.rerun()


# -------- PAGE 2 --------
elif st.session_state.page == 2:
    st.markdown(
        """
        <h2 style='text-align: center;'>Hey Love ❤️</h2>
        """,
        unsafe_allow_html=True
    )

    name = st.text_input("Her Name 💖")

    message = st.text_area(
        "My Apology 💌",
        "I know I hurt you, and I hate that I did. You mean everything to me. "
        "Please give me one chance to make things right. I promise I'll do better ❤️"
    )

    if st.button("Show My Heart 💖"):
        st.session_state.page = 3
        st.session_state.name = name
        st.session_state.message = message
        st.rerun()


# -------- PAGE 3 --------
elif st.session_state.page == 3:
    st.balloons()

    st.markdown(
        f"""
        <div style='text-align: center;'>
            <h2>Dear {st.session_state.get("name", "Love")} ❤️</h2>
            <p style='font-size:20px;'>{st.session_state.get("message")}</p>
            <br>
            <h3>I’m really sorry... please forgive me 💔</h3>
            <h1>❤️ ❤️ ❤️</h1>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Start Again 🔄"):
        st.session_state.page = 1
        st.rerun()
