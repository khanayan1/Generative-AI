import streamlit as st
import time

st.set_page_config(page_title="Sorry ❤️", page_icon="💔")

# Session state
if "page" not in st.session_state:
    st.session_state.page = 1

# -------- PAGE 1 --------
if st.session_state.page == 1:
    st.markdown("""
        <h1 style='text-align:center; font-size:90px; color:red;'>
        💔 SORRY 💔
        </h1>
        <h3 style='text-align:center;'>I never meant to hurt you...</h3>
    """, unsafe_allow_html=True)

    st.write("")

    if st.button("Tap to open my heart ❤️"):
        with st.spinner("Opening my heart..."):
            time.sleep(2)
        st.session_state.page = 2
        st.rerun()


# -------- PAGE 2 --------
elif st.session_state.page == 2:
    st.markdown("<h2 style='text-align:center;'>Enter Your Name 💖</h2>", unsafe_allow_html=True)

    name = st.text_input("")

    if st.button("Continue ❤️"):
        if name.strip().upper() != "BINTA":
            st.error("Only my love can enter… ❤️")
        else:
            st.session_state.page = 3
            st.rerun()


# -------- PAGE 3 (HEART OPENING EFFECT) --------
elif st.session_state.page == 3:

    # Heart animation using HTML + CSS
    st.markdown("""
        <style>
        .heart {
            width: 100px;
            height: 100px;
            position: relative;
            margin: auto;
            animation: beat 1s infinite;
        }

        .heart:before, .heart:after {
            content: "";
            width: 100px;
            height: 100px;
            position: absolute;
            left: 50px;
            top: 0;
            background: red;
            border-radius: 50px 50px 0 0;
            transform: rotate(-45deg);
            transform-origin: 0 100%;
        }

        .heart:after {
            left: 0;
            transform: rotate(45deg);
            transform-origin: 100% 100%;
        }

        @keyframes beat {
            0% { transform: scale(1); }
            50% { transform: scale(1.2); }
            100% { transform: scale(1); }
        }

        .fade-in {
            animation: fadeIn 3s ease-in;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
        </style>

        <div class="heart"></div>
    """, unsafe_allow_html=True)

    time.sleep(2)

    st.markdown("""
        <div class="fade-in" style='text-align:center;'>
            <h2>Dear Binta ❤️</h2>
            <p style='font-size:20px;'>
            I know I hurt you, and I regret it deeply...  
            You are very special to me, and I never want to lose you.  
            Please forgive me and give me one chance to make everything right. 💔  
            </p>
            <h3>I’m truly sorry... ❤️</h3>
        </div>
    """, unsafe_allow_html=True)

    st.balloons()
