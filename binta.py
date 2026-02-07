import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="My Feelings ❤️",
    page_icon="❤️",
    layout="centered"
)

# -----------------------------
# Session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# -----------------------------
# LOGIN PAGE
if not st.session_state.logged_in:
    st.markdown("""
        <style>
        body {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            font-family: 'Poppins', sans-serif;
        }
        .login-box {
            display:flex;
            flex-direction:column;
            justify-content:center;
            align-items:center;
            height:90vh;
            text-align:center;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="login-box">
            <h1>💌 Welcome</h1>
            <p>Enter the secret password</p>
        </div>
    """, unsafe_allow_html=True)

    password = st.text_input("Password", type="password")

    if st.button("Login ❤️", use_container_width=True):
        if password.strip().lower() == "i love you":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Wrong password 💔")

# -----------------------------
# MAIN PAGE
else:
    html_code = """
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
    body {
        margin:0;
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(135deg, #fbc2eb, #a6c1ee);
        display:flex;
        flex-direction:column;
        align-items:center;
    }

    h1 {
        color:white;
        text-align:center;
        margin:30px 10px;
        font-size:1.4rem;
    }

    .container {
        width:100%;
        max-width:420px;
        padding-bottom:120px;
    }

    .card {
        width:90%;
        height:190px;
        margin:15px auto;
        perspective:1000px;
    }

    .card-inner {
        width:100%;
        height:100%;
        position:relative;
        transition:transform 0.6s;
        transform-style:preserve-3d;
        border-radius:25px;
        box-shadow:0 10px 25px rgba(0,0,0,0.25);
    }

    .card.flipped .card-inner {
        transform:rotateY(180deg);
    }

    .front, .back {
        position:absolute;
        width:100%;
        height:100%;
        border-radius:25px;
        backface-visibility:hidden;
        display:flex;
        justify-content:center;
        align-items:center;
        text-align:center;
        padding:20px;
        font-size:1rem;
        flex-direction:column;
    }

    .front {
        background: linear-gradient(135deg, #89f7fe, #66a6ff);
        color:white;
        font-weight:600;
    }

    .back {
        background: linear-gradient(135deg, #ff9a9e, #fecfef);
        color:#333;
        transform:rotateY(180deg);
        line-height:1.6;
    }

    /* Love Question */
    .love-box {
        margin:30px auto;
        width:90%;
        background:rgba(255,255,255,0.35);
        padding:25px;
        border-radius:25px;
        text-align:center;
        position:relative;
    }

    .love-box h2 {
        color:white;
        margin-bottom:20px;
        font-size:1.2rem;
    }

    .btn {
        padding:12px 22px;
        font-size:1rem;
        border:none;
        border-radius:18px;
        cursor:pointer;
        margin:10px;
    }

    .yes {
        background:#ff4b5c;
        color:white;
        width:120px;
    }

    .no {
        background:white;
        color:#333;
        position:absolute;
        left:50%;
        transform:translateX(-50%);
        width:100px;
    }
    </style>

    <h1>Things I Feel When I Think of You 🌷</h1>

    <div class="container">

        <div class="card" onclick="this.classList.toggle('flipped')">
            <div class="card-inner">
                <div class="front">💬 What is Love?</div>
                <div class="back">💞 Door hoke bhi dil saath rehta hai ❤️</div>
            </div>
        </div>

        <div class="card" onclick="this.classList.toggle('flipped')">
            <div class="card-inner">
                <div class="front">🌙 What You Mean to Me</div>
                <div class="back">💖 Tum meri zindagi ka sabse khoobsurat hissa ho</div>
            </div>
        </div>

        <div class="card" onclick="this.classList.toggle('flipped')">
            <div class="card-inner">
                <div class="front">🌈 When I Think of You</div>
                <div class="back">🌸 Ek ajeeb si khushi hoti hai</div>
            </div>
        </div>

        <div class="card" onclick="this.classList.toggle('flipped')">
            <div class="card-inner">
                <div class="front">💐 My Promise</div>
                <div class="back">💖 Main hamesha saath rahunga</div>
            </div>
        </div>

        <div class="love-box">
            <h2>Do you love me? 💖</h2>
            <button class="btn yes" onclick="alert('I knew it 😍❤️')">Yes</button>
            <button class="btn no" id="noBtn">No</button>
        </div>

    </div>

    <script>
    const noBtn = document.getElementById("noBtn");

    function moveNo(){
        const box = document.querySelector('.love-box');
        const maxX = box.clientWidth - 120;
        const maxY = 80;

        const x = Math.random() * maxX;
        const y = Math.random() * maxY;

        noBtn.style.left = x + "px";
        noBtn.style.top = y + "px";
    }

    noBtn.addEventListener("touchstart", moveNo);
    noBtn.addEventListener("mouseover", moveNo);
    </script>
    """

    components.html(html_code, height=1400)
