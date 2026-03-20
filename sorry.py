import streamlit as st

# Page config
st.set_page_config(page_title="I'm Sorry ❤️", page_icon="💔")

# Title
st.title("I'm Really Sorry ❤️")

# Subtitle
st.subheader("I know I messed up... 😔")

# Input your GF's name
name = st.text_input("Enter her name:", "")

# Message input
message = st.text_area("Write your apology message:", 
                       "I’m really sorry for what I did. You mean a lot to me and I never want to hurt you. Please forgive me ❤️")

# Button to show message
if st.button("Send Apology 💌"):
    if name:
        st.markdown(f"""
        ### Dear {name} ❤️

        {message}

        ---
        I promise to be better and make you smile again 😊  
        Please forgive me 💖
        """)
    else:
        st.warning("Please enter her name 😅")

# Cute extra section
st.write("---")
st.caption("Made with love by someone who really cares 💞")
