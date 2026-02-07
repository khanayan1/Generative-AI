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
            height:50vh;
            text-align:center;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="login-box">
            <h1>💌 Welcome My Love...</h1>
            <p>Hint :- Something I never get tired of saying</p>
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
        font-family:'Poppins', sans-serif;
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
        padding-bottom:140px;
    }

    /* Single Card */
    .card {
        width:90%;
        height:260px;
        margin:20px auto;
        perspective:1000px;
    }

    .card-inner {
        width:100%;
        height:100%;
        position:relative;
        transition:transform 0.6s;
        transform-style:preserve-3d;
        border-radius:25px;
        box-shadow:0 12px 30px rgba(0,0,0,0.25);
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
        padding:25px;
        flex-direction:column;
        line-height:1.6;
    }

    .front {
        background: linear-gradient(135deg, #89f7fe, #66a6ff);
        color:white;
        font-size:1.1rem;
        font-weight:600;
    }

    .back {
        background: linear-gradient(135deg, #ff9a9e, #fecfef);
        color:#333;
        transform:rotateY(180deg);
        font-size:0.95rem;
    }

    /* Love Question */
    .love-box {
        margin-top:50px;
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
        margin-bottom:25px;
        font-size:1.2rem;
    }

    .btn-container {
        display:flex;
        justify-content:center;
        gap:40px;
        position:relative;
    }

    .btn {
        padding:12px 24px;
        font-size:1rem;
        border:none;
        border-radius:20px;
        cursor:pointer;
    }

    .yes {
        background:#ff4b5c;
        color:white;
    }

    .no {
        background:white;
        color:#333;
        position:relative;
    }
    </style>

    <h1>I love You Binta(Queen) 💖</h1>

    <div class="container">

        <!-- Single Card -->
        <div class="card" onclick="this.classList.toggle('flipped')">
            <div class="card-inner">
                <div class="front">
                    💌 Tap to Read
                </div>
                <div class="back">
                    ✨ Teri aankhein batati hain, tujhe mujh se mohabbat hai<br>
                    💞 Par dil ki tashali ke liye, izhaar ho jaaye<br>
                    <br>
                    Abhi tohh bol doo....

                    
                    <br><br>
                    

                    🌙 So just a small reminder…<br><br>

                    💫 We’ve already done the hardest part —<br>
                    finding each other among the millions of people<br><br>

                    🌷 Now let’s do the easiest thing…<br>
                    ❤️ Never lose each other.
                    
                </div>
            </div>
        </div>

        <!-- Question -->
        <div class="love-box">
            <h2>Do you love me? 💖</h2>
            <div class="btn-container">
                <button class="btn yes" onclick="yesClicked()">Yes</button>
                <button class="btn no" id="noBtn">No</button>
            </div>
        </div>

    </div>

    <script>
    function yesClicked(){
        alert("💍 Now you are booked for lifetime ❤️\\nCongratulations 🎉");
    }

    const noBtn = document.getElementById("noBtn");

    function moveNo(){
        const x = Math.random() * 120 - 60;
        const y = Math.random() * 80 - 40;
        noBtn.style.transform = `translate(${x}px, ${y}px)`;
    }

    noBtn.addEventListener("touchstart", moveNo);
    noBtn.addEventListener("mouseover", moveNo);
    </script>
    """

    components.html(html_code, height=1300)
