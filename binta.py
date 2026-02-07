import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="My Love ❤️",
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
            <p><b>Hint 🧩</b><br>
            Something I never get tired of saying ❤️</p>
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
        overflow-x:hidden;
    }

    /* Scrolling I LOVE YOU */
    .marquee {
        width:100%;
        overflow:hidden;
        white-space:nowrap;
        color:white;
        font-size:1.2rem;
        margin-top:10px;
    }
    .marquee span {
        display:inline-block;
        padding-left:100%;
        animation: scroll 10s linear infinite;
    }
    @keyframes scroll {
        0% { transform: translateX(0); }
        100% { transform: translateX(-100%); }
    }

    h1 {
        color:white;
        text-align:center;
        margin:20px 10px;
        font-size:1.4rem;
    }

    .container {
        max-width:420px;
        margin:auto;
        padding-bottom:180px;
    }

    /* Card */
    .card {
        width:90%;
        height:260px;
        margin:30px auto;
        perspective:1000px;
    }

    .card-inner {
        width:100%;
        height:100%;
        transition:transform 0.6s;
        transform-style:preserve-3d;
        position:relative;
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
        margin-top:80px;
        width:90%;
        margin-left:auto;
        margin-right:auto;
        background:rgba(255,255,255,0.35);
        padding:25px;
        border-radius:25px;
        text-align:center;
    }

    .btn-container {
        display:flex;
        justify-content:center;
        gap:50px;
        margin-top:20px;
    }

    .btn {
        padding:12px 28px;
        border:none;
        border-radius:20px;
        font-size:1rem;
        cursor:pointer;
    }

    .yes {
        background:#ff4b5c;
        color:white;
    }

    .no {
        background:white;
        position:relative;
    }

    /* Popup */
    .popup {
        position:fixed;
        top:0;
        left:0;
        width:100%;
        height:100%;
        background:rgba(0,0,0,0.5);
        display:none;
        justify-content:center;
        align-items:center;
        z-index:999;
    }

    .popup-box {
        background:white;
        padding:30px;
        border-radius:25px;
        text-align:center;
        animation:pop 0.4s ease;
    }

    @keyframes pop {
        from {transform:scale(0.6); opacity:0;}
        to {transform:scale(1); opacity:1;}
    }

    .popup-box button {
        margin-top:20px;
        padding:10px 25px;
        border:none;
        border-radius:20px;
        background:#ff4b5c;
        color:white;
        font-size:1rem;
        cursor:pointer;
    }

    /* Confetti */
    .confetti {
        position:fixed;
        width:10px;
        height:10px;
        top:0;
        animation:fall 3s linear forwards;
    }

    @keyframes fall {
        to {
            transform:translateY(100vh) rotate(360deg);
            opacity:0;
        }
    }
    </style>

    <div class="marquee">
        <span>❤️ I LOVE YOU ❤️ I LOVE YOU ❤️ I LOVE YOU ❤️</span>
    </div>

    <h1>I love You Binta (Queen) 💖</h1>

    <div class="container">

        <div class="card" onclick="this.classList.toggle('flipped')">
            <div class="card-inner">
                <div class="front">💌 Tap to Read</div>
                <div class="back">
                    ✨ Teri aankhein batati hain, tujhe mujh se mohabbat hai<br>
                    💞 Par dil ki tasalli ke liye, izhaar ho jaaye<br><br>
                    Abhi tohh bol doo…<br><br>
                    🌙 We’ve already done the hardest part —<br>
                    finding each other among millions<br><br>
                    ❤️ Never lose each other.
                </div>
            </div>
        </div>

        <div class="love-box">
            <h2>Do you love me? 💖</h2>
            <div class="btn-container">
                <button class="btn yes" onclick="yesClicked()">Yes</button>
                <button class="btn no" id="noBtn">No</button>
            </div>
        </div>
    </div>

    <div id="popup" class="popup">
        <div class="popup-box">
            <h2>💍 Congratulations!</h2>
            <p>Now you are booked for lifetime ❤️</p>
            <button onclick="closePopup()">OK 💖</button>
        </div>
    </div>

    <script>
    function yesClicked(){
        document.getElementById("popup").style.display="flex";
        for(let i=0;i<80;i++){
            const c=document.createElement("div");
            c.className="confetti";
            c.style.left=Math.random()*100+"vw";
            c.style.backgroundColor=["#ff4b5c","#ffd700","#6a5acd","#00c9a7"][Math.floor(Math.random()*4)];
            c.style.animationDuration=(Math.random()*2+2)+"s";
            document.body.appendChild(c);
            setTimeout(()=>c.remove(),3000);
        }
    }

    function closePopup(){
        document.getElementById("popup").style.display="none";
    }

    const noBtn=document.getElementById("noBtn");
    function moveNo(){
        const x=Math.random()*400-200;
        const y=Math.random()*250-120;
        noBtn.style.transform=`translate(${x}px,${y}px)`;
    }
    noBtn.addEventListener("mouseover",moveNo);
    noBtn.addEventListener("touchstart",moveNo);
    </script>
    """

    components.html(html_code, height=1400)
