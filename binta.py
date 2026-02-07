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
# MAIN PAGE (AFTER LOGIN)
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
      text-shadow:0 3px 8px rgba(0,0,0,0.2);
      text-align:center;
    }

    .tab-container {
      display:flex;
      gap:20px;
      flex-wrap:wrap;
      justify-content:center;
      margin-top:40px;
      width:100%;
      padding-bottom:100px;
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

    .bottom-bar {
      position:fixed;
      bottom:0;
      left:0;
      width:100%;
      display:flex;
      justify-content:space-around;
      padding:10px 0;
      background:rgba(255,255,255,0.3);
      backdrop-filter:blur(10px);
      box-shadow:0 -2px 10px rgba(0,0,0,0.2);
    }

    .bottom-bar button {
      padding:8px 14px;
      border-radius:12px;
      border:none;
      background:white;
      font-weight:600;
      cursor:pointer;
    }
    </style>

    <h1>Things I Feel When I Think of You 🌷</h1>

    <div class="tab-container">

      <div class="tab" id="tab1" onclick="this.classList.toggle('flipped')">
        <div class="tab-inner">
          <div class="front">💬 What is Love?</div>
          <div class="back">
            🌸 Pyaar sirf paas rehna nahi hota<br>
            💞 Door hoke bhi dil saath rehta hai<br>
            ❤️ Wahi pyaar hai
          </div>
        </div>
      </div>

      <div class="tab" id="tab2" onclick="this.classList.toggle('flipped')">
        <div class="tab-inner">
          <div class="front">🌙 What You Mean to Me</div>
          <div class="back">
            💖 Tum meri zindagi ka sabse khoobsurat hissa ho<br>
            🌷 Har pal tum yaad aate ho
          </div>
        </div>
      </div>

      <div class="tab" id="tab3" onclick="this.classList.toggle('flipped')">
        <div class="tab-inner">
          <div class="front">🌈 When I Think of You</div>
          <div class="back">
            🌸 Ek ajeeb si khushi hoti hai<br>
            💞 Bas milne ka mann karta hai
          </div>
        </div>
      </div>

      <div class="tab" id="tab4" onclick="this.classList.toggle('flipped')">
        <div class="tab-inner">
          <div class="front">💐 My Promise</div>
          <div class="back">
            💖 Main hamesha saath rahunga<br>
            🌹 Khushi ho ya udaasi
          </div>
        </div>
      </div>

    </div>

    <div class="bottom-bar">
      <button onclick="scrollToTab('tab1')">💬 Love</button>
      <button onclick="scrollToTab('tab2')">🌙 Meaning</button>
      <button onclick="scrollToTab('tab3')">🌈 Thinking</button>
      <button onclick="scrollToTab('tab4')">💐 Promise</button>
    </div>

    <script>
    function scrollToTab(id){
        const tab = document.getElementById(id);
        tab.scrollIntoView({behavior:'smooth', block:'center'});
        tab.classList.add('flipped');
        setTimeout(()=>{tab.classList.remove('flipped');}, 4000);
    }
    </script>
    """

    components.html(html_code, height=1000)
