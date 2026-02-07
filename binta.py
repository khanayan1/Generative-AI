import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="My Feelings ❤️", page_icon="❤️", layout="wide")

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
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown(
        "<div class='login-box'><h1>💌 Welcome</h1><p>Enter the password to continue</p></div>",
        unsafe_allow_html=True
    )

    password = st.text_input("Password", type="password")

    if st.button("Login ❤️"):
        if password.strip().lower() == "i love you":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Wrong password 💔")

# -----------------------------
# MAIN PAGE
else:
    html_code = """
    <style>
    body {
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(135deg, #fbc2eb, #a6c1ee);
      margin:0;
      padding:0;
      display:flex;
      flex-direction:column;
      align-items:center;
    }

    h1 {
      margin-top:40px;
      color:#fff;
      text-align:center;
      text-shadow:0 3px 8px rgba(0,0,0,0.2);
    }

    .tab-container {
      display:flex;
      gap:20px;
      flex-wrap:wrap;
      justify-content:center;
      margin-top:40px;
      width:100%;
      padding-bottom:120px;
    }

    .tab {
      width:90%;
      max-width:350px;
      height:200px;
      cursor:pointer;
      perspective:1000px;
    }

    .tab-inner {
      position:relative;
      width:100%;
      height:100%;
      border-radius:25px;
      box-shadow:0 10px 25px rgba(0,0,0,0.2);
      transition:transform 0.6s;
      transform-style:preserve-3d;
    }

    .tab.flipped .tab-inner {
      transform:rotateY(180deg);
    }

    .front, .back {
      position:absolute;
      width:100%;
      height:100%;
      backface-visibility:hidden;
      border-radius:25px;
      display:flex;
      justify-content:center;
      align-items:center;
      text-align:center;
      padding:20px;
      flex-direction:column;
    }

    .front {
      background: linear-gradient(135deg, #89f7fe, #66a6ff);
      color:white;
      font-size:1.1em;
    }

    .back {
      background: linear-gradient(135deg, #ff9a9e, #fecfef);
      color:#333;
      transform:rotateY(180deg);
      font-size:0.95em;
      line-height:1.5em;
    }

    /* Love Question */
    .love-box {
      margin-top:40px;
      background:rgba(255,255,255,0.3);
      padding:30px;
      border-radius:25px;
      text-align:center;
      box-shadow:0 10px 25px rgba(0,0,0,0.2);
      position:relative;
      width:90%;
      max-width:350px;
    }

    .love-box h2 {
      color:white;
      margin-bottom:20px;
    }

    .btn {
      padding:10px 20px;
      border:none;
      border-radius:15px;
      font-size:1em;
      cursor:pointer;
      margin:10px;
    }

    .yes {
      background:#ff4b5c;
      color:white;
    }

    .no {
      background:#fff;
      position:absolute;
    }

    </style>

    <h1>Things I Feel When I Think of You 🌷</h1>

    <div class="tab-container">

      <div class="tab" onclick="this.classList.toggle('flipped')">
        <div class="tab-inner">
          <div class="front">💬 What is Love?</div>
          <div class="back">
            💞 Door hoke bhi dil saath rehta hai<br>
            ❤️ Wahi pyaar hai
          </div>
        </div>
      </div>

      <div class="tab" onclick="this.classList.toggle('flipped')">
        <div class="tab-inner">
          <div class="front">🌙 What You Mean to Me</div>
          <div class="back">
            💖 Tum meri zindagi ka sabse khoobsurat hissa ho
          </div>
        </div>
      </div>

      <div class="tab" onclick="this.classList.toggle('flipped')">
        <div class="tab-inner">
          <div class="front">🌈 When I Think of You</div>
          <div class="back">
            🌸 Ek ajeeb si khushi hoti hai
          </div>
        </div>
      </div>

      <div class="tab" onclick="this.classList.toggle('flipped')">
        <div class="tab-inner">
          <div class="front">💐 My Promise</div>
          <div class="back">
            💖 Main hamesha saath rahunga
          </div>
        </div>
      </div>

      <!-- Love Question -->
      <div class="love-box">
        <h2>Do you love me? 💖</h2>
        <button class="btn yes" onclick="alert('I knew it 😍❤️')">Yes</button>
        <button class="btn no" id="noBtn">No</button>
      </div>

    </div>

    <script>
    const noBtn = document.getElementById("noBtn");

    noBtn.addEventListener("mouseover", moveButton);
    noBtn.addEventListener("touchstart", moveButton);

    function moveButton(){
        const x = Math.random() * 200 - 100;
        const y = Math.random() * 150 - 75;
        noBtn.style.transform = `translate(${x}px, ${y}px)`;
    }
    </script>
    """

    components.html(html_code, height=1200)
