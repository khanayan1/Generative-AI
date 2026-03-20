import streamlit as st
import time
import re

# Page config
st.set_page_config(page_title="Sorry ❤️", page_icon="💔")

# Session state
if "page" not in st.session_state:
    st.session_state.page = 1


# -------- PAGE 1 (ENTRY) --------
if st.session_state.page == 1:
    st.markdown("""
        <h1 style='text-align:center; font-size:90px; color:#ff4b5c;'>
        💔 SORRY 💔
        </h1>
        <h3 style='text-align:center; color:gray;'>
        I never meant to hurt you...
        </h3>
    """, unsafe_allow_html=True)

    st.write("")
    st.write("")

    if st.button("Tap to open my heart ❤️"):
        with st.spinner("Opening my heart..."):
            time.sleep(2)
        st.session_state.page = 2
        st.rerun()


# -------- PAGE 2 (NAME CHECK) --------
elif st.session_state.page == 2:
    st.markdown("<h2 style='text-align:center;'>Only for someone special 💖</h2>", unsafe_allow_html=True)

    name = st.text_input("Enter your name")

    if st.button("Continue ❤️"):
        # strict validation (only BINTA)
        if not re.fullmatch(r"\s*binta\s*", name, re.IGNORECASE):
            st.error("This page is only for my love… ❤️")
        else:
            with st.spinner("Let me show you how I feel..."):
                time.sleep(2)
            st.session_state.page = 3
            st.rerun()


# -------- PAGE 3 (HEART + MESSAGE) --------
elif st.session_state.page == 3:

    st.markdown("""
    <style>
    body {
        background-color: #0e1117;
    }

    .heart-container {
        display:flex;
        justify-content:center;
        align-items:center;
        height:200px;
        margin-top:20px;
        animation: fadeIn 2s ease-in;
    }

    .heart {
        width:120px;
        height:120px;
        position: relative;
        transform: rotate(-45deg);
        background: #ff4b5c;
        animation: pulse 1.2s infinite;
        border-radius: 20px;
    }

    .heart:before,
    .heart:after {
        content: "";
        position: absolute;
        width:120px;
        height:120px;
        background:#ff4b5c;
        border-radius:50%;
    }

    .heart:before {
        top:-60px;
        left:0;
    }

    .heart:after {
        left:60px;
        top:0;
    }

    @keyframes pulse {
        0% { transform: rotate(-45deg) scale(1); }
        50% { transform: rotate(-45deg) scale(1.25); }
        100% { transform: rotate(-45deg) scale(1); }
    }

    .message {
        text-align:center;
        font-size:22px;
        line-height:1.7;
        margin-top:30px;
        color:white;
        animation: fadeInText 3s ease-in;
        padding: 0 20px;
    }

    @keyframes fadeInText {
        from { opacity:0; transform: translateY(20px); }
        to { opacity:1; transform: translateY(0); }
    }

    </style>

    <div class="heart-container">
        <div class="heart"></div>
    </div>
    """, unsafe_allow_html=True)

    # dramatic pause
    time.sleep(2)

    st.markdown("""
    <div class="message">
        <h2>Dear Binta ❤️</h2>

        
        I’ve been thinking about everything… and honestly, it hurts knowing that I hurt you.
        That was never my intention.
        

       
        You mean more to me than I’m able to express sometimes, and maybe that’s where I go wrong…
        but my feelings for you are real, always have been.
        

        
        I miss your smile, your presence, your energy…
        and I really don’t want to lose your smile love...
        

        
        I’m truly sorry… not just in words, but from my heart.  
        Please forgive me ❤️
       
    </div>
    """, unsafe_allow_html=True)

    st.balloons()
