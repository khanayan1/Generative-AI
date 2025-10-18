import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="My Feelings ❤️", page_icon="❤️", layout="wide")

# -----------------------------
# Session state for login
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# -----------------------------
# LOGIN PAGE
if not st.session_state.logged_in:
    st.markdown("""
        <style>
        body {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            font-family: 'Poppins', sans-serif;
            color: #333;
        }
        .login-box {
            display:flex; flex-direction:column; justify-content:center; align-items:center; height:90vh;
        }
        input {
            padding:10px 15px; border-radius:10px; border:2px solid #fff; font-size:1em; outline:none;
            width: 80%;
            max-width: 300px;
        }
        button {
            background-color:#ff4b5c; border:none; color:white; padding:10px 20px; font-size:1em; border-radius:10px;
            margin-top:20px; cursor:pointer; transition:0.3s;
        }
        button:hover {transform: scale(1.05);}
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<div class='login-box'><h1>💌 Welcome</h1><p>Enter your name to continue</p></div>", unsafe_allow_html=True)
    name = st.text_input("Your Name")
    if st.button("Submit ❤️"):
        if name.strip():
            st.session_state.logged_in = True
            st.session_state.user_name = name.strip()
            st.rerun()
        else:
            st.warning("Please enter your name 😊")

# -----------------------------
# MAIN PAGE (AFTER LOGIN)
else:
    user_name = st.session_state.user_name

    html_code = f"""
    <style>
    body {{
      font-family: 'Poppins', sans-serif;
      background: linear-gradient(135deg, #fbc2eb, #a6c1ee);
      margin:0; padding:0; display:flex; flex-direction:column; align-items:center;
    }}

    .user-name {{
      position: fixed; top:20px; right:15px; background: rgba(255,255,255,0.3);
      padding: 8px 15px; border-radius:15px; font-weight:600; color:#fff;
      box-shadow:0 4px 10px rgba(0,0,0,0.2); backdrop-filter: blur(8px); font-size:0.9em;
    }}

    h1 {{
      margin-top:60px; color:#fff; text-shadow:0 3px 8px rgba(0,0,0,0.2);
      font-size:1.5em;
      text-align:center;
      padding: 0 15px;
    }}

    .tab-container {{
      display: flex;
      gap: 20px;
      flex-wrap: wrap;
      justify-content: center;
      margin-top:40px;
      perspective: 1000px;
      width: 100%;
      padding: 0 10px;
    }}

    .tab {{
      width: 90%;
      max-width: 350px;
      height: 200px;
      cursor: pointer;
      position: relative;
      transition: transform 0.6s;
      transform-style: preserve-3d;
      margin-bottom: 20px;
    }}

    .tab-inner {{
      position: relative;
      width: 100%;
      height: 100%;
      border-radius: 25px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.2);
      transition: transform 0.6s;
      transform-style: preserve-3d;
    }}

    .tab:hover .tab-inner {{
      transform: rotateY(5deg) rotateX(3deg);
    }}

    .tab.flipped .tab-inner {{
      transform: rotateY(180deg);
    }}

    .front, .back {{
      position: absolute;
      width: 100%;
      height: 100%;
      backface-visibility: hidden;
      border-radius: 25px;
      display: flex;
      justify-content: center;
      align-items: center;
      text-align: center;
      padding: 20px;
      font-size: 1em;
      flex-direction: column;
    }}

    .front {{
      background: linear-gradient(135deg, #89f7fe, #66a6ff);
      color: white;
    }}

    .back {{
      background: linear-gradient(135deg, #ff9a9e, #fecfef);
      color: #333;
      transform: rotateY(180deg);
      overflow-y: auto;
      font-size: 0.95em;
      line-height: 1.5em;
    }}

    .corner-heart {{
      position: fixed; font-size: 2em; opacity:0.4; animation: float 4s ease-in-out infinite;
    }}
    .corner1 {{ top: 10px; left: 15px; color:#fff; }}
    .corner2 {{ bottom: 10px; right: 15px; color:#fff; animation-delay: 2s; }}

    @keyframes float {{
      0%, 100% {{ transform: translateY(0); opacity:0.5; }}
      50% {{ transform: translateY(-10px); opacity:1; }}
    }}

    /* Bottom mobile nav bar */
    .bottom-bar {{
      position: fixed;
      bottom: 0;
      left: 0;
      width: 100%;
      display: flex;
      justify-content: space-around;
      padding: 8px 0;
      background: rgba(255,255,255,0.2);
      backdrop-filter: blur(10px);
      box-shadow: 0 -2px 10px rgba(0,0,0,0.2);
      z-index: 100;
    }}

    .bottom-bar button {{
      padding: 8px 12px;
      border-radius: 12px;
      border: none;
      background: rgba(255,255,255,0.4);
      color: #333;
      font-weight: 600;
      font-size: 0.9em;
      cursor: pointer;
      transition: 0.3s;
    }}

    .bottom-bar button:hover {{
      background: rgba(255,255,255,0.7);
      transform: scale(1.05);
    }}
    </style>

    <div class="user-name">Hi, {user_name} 💖</div>
    <div class="corner-heart corner1">💞</div>
    <div class="corner-heart corner2">🌸</div>

    <h1>Things I Feel When I Think of You 🌷</h1>

    <div class="tab-container">
      <div class="tab" id="tab1" onclick="this.classList.toggle('flipped')">
        <div class="tab-inner">
          <div class="front">💬 What is Love?</div>
          <div class="back">
            🌸 Jab tumse mile, tab samajh aaya...<br>
            💞 Pyaar sirf saath rehne ka naam nahi hota<br>
            🌷 Kabhi paas ho ya door, farq padta hi nahi...<br>
            🌞 Bas har subah jab aankh khule, sabse pehle tum yaad aa jao —<br>
            ❤️ Wahi toh pyaar hai 💓
          </div>
        </div>
      </div>

      <div class="tab" id="tab2" onclick="this.classList.toggle('flipped')">
        <div class="tab-inner">
          <div class="front">🌙 What You Mean to Me</div>
          <div class="back">
            ✨ Isko words me likhna mere liye possible nhi hai...<br>
            💖 Bas tum meri zindagi ka sabse khoobsurat hissa ho<br>
            🌹 Har pal tumhari yaadein mere saath hain
          </div>
        </div>
      </div>

      <div class="tab" id="tab3" onclick="this.classList.toggle('flipped')">
        <div class="tab-inner">
          <div class="front">🌈 When I Think of You</div>
          <div class="back">
            🌞 Phle toh dimag se nahi niklti...<br>
            🌸 Par jab sochta ho tumhare baare me...<br>
            💞 Ek ajeeb si khushi hoti hai, lagta hai ab itni dur kya kar rhi ho...<br>
            🌷 Jaldi se milo mujhe...
          </div>
        </div>
      </div>

      <div class="tab" id="tab4" onclick="this.classList.toggle('flipped')">
        <div class="tab-inner">
          <div class="front">💐 My Promise</div>
          <div class="back">
            💖 Main hamesha tumhare saath rahu, khushi me ya udaasi me 💫<br>
            🌹 Kabhi muskuraane ka reason ban jaun, kabhi bas chup-chaap tumhara saaya 💕<br>
            🌸 Per bas chipka rho 💞
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom mobile nav bar -->
    <div class="bottom-bar">
      <button onclick="scrollToTab('tab1')">💬 Love</button>
      <button onclick="scrollToTab('tab2')">🌙 You Mean</button>
      <button onclick="scrollToTab('tab3')">🌈 Thinking</button>
      <button onclick="scrollToTab('tab4')">💐 Promise</button>
    </div>

    <script>
    function scrollToTab(tabId){{
        const tab = document.getElementById(tabId);
        tab.scrollIntoView({{behavior:'smooth', block:'center'}});
        tab.classList.add('flipped');
        setTimeout(()=>{{ tab.classList.remove('flipped'); }}, 4000);
    }}
    </script>
    """

    components.html(html_code, height=900)
