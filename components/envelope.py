import streamlit as st
import base64
from pathlib import Path


# =====================================================
# IMAGE LOADER
# =====================================================

def load_image(path):

    file = Path(path)

    if not file.exists():
        return None

    return base64.b64encode(file.read_bytes()).decode()


# =====================================================
# ENVELOPE PAGE
# =====================================================

def envelope_page():

    background = load_image(
        "assets/images/letter_background.png"
    )

    closed = load_image(
        "assets/images/closed_envelope.png"
    )

    opened = load_image(
        "assets/images/open_envelope.png"
    )

    half = load_image(
        "assets/images/letter_half_out.png"
    )

    petals = load_image(
        "assets/images/petals.png"
    )

    sparkles = load_image(
        "assets/images/sparkles.png"
    )

    # =====================================================
    # BACKGROUND
    # =====================================================

    if background:

        st.markdown(
            f"""
<style>

.stApp{{
background-image:url("data:image/png;base64,{background}");
background-size:cover;
background-position:center;
background-repeat:no-repeat;
background-attachment:fixed;
}}

</style>
""",
            unsafe_allow_html=True,
        )

    # =====================================================
    # CSS
    # =====================================================

    st.markdown(
        """
<style>

header{
visibility:hidden;
}

footer{
visibility:hidden;
}

#MainMenu{
visibility:hidden;
}

.main > div{
padding-top:0rem;
}

@keyframes fadeIn{

from{
opacity:0;
transform:translateY(50px);
}

to{
opacity:1;
transform:translateY(0px);
}

}

@keyframes float{

0%{
transform:translateY(0px);
}

50%{
transform:translateY(-12px);
}

100%{
transform:translateY(0px);
}

}

@keyframes glow{

0%{
box-shadow:0 0 15px rgba(255,255,255,.35);
}

50%{
box-shadow:0 0 45px rgba(255,255,255,.85);
}

100%{
box-shadow:0 0 15px rgba(255,255,255,.35);
}

}

.title{

font-size:58px;
font-weight:800;
color:white;
text-align:center;
margin-top:35px;
text-shadow:3px 3px 20px black;
animation:fadeIn 2s;

}

.subtitle{

font-size:22px;
text-align:center;
color:white;
margin-bottom:45px;
animation:fadeIn 2.5s;

}

.card{

width:760px;

margin:auto;

padding:35px;

border-radius:28px;

background:rgba(255,255,255,.18);

backdrop-filter:blur(20px);

border:1px solid rgba(255,255,255,.35);

box-shadow:0 12px 40px rgba(0,0,0,.35);

animation:fadeIn 2s;

}

.envelope{

display:block;

margin:auto;

width:360px;

animation:float 5s infinite;

}

.message{

color:white;

text-align:center;

font-size:22px;

margin-top:30px;

line-height:40px;

}

div.stButton > button{

height:58px;

font-size:22px;

font-weight:bold;

border-radius:16px;

background:#d62839;

color:white;

border:none;

animation:glow 2s infinite;

}

div.stButton > button:hover{

background:#b00020;

transform:scale(1.02);

}

</style>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # HEADER
    # =====================================================

    st.markdown(
        """
<div class="title">
💌 A Letter From My Heart
</div>

<div class="subtitle">
Some feelings are too beautiful to be spoken...
So I wrote them for you.
</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # GLASS CARD
    # =====================================================

    st.markdown(
        """
<div class="card">
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # SHOW ENVELOPE
    # =====================================================

    if "envelope_state" not in st.session_state:
        st.session_state.envelope_state = "closed"

    current = st.session_state.envelope_state

    if current == "closed" and closed:

        st.markdown(
            f"""
<img
class="envelope"
src="data:image/png;base64,{closed}">
""",
            unsafe_allow_html=True,
        )

    elif current == "opened" and opened:

        st.markdown(
            f"""
<img
class="envelope"
src="data:image/png;base64,{opened}">
""",
            unsafe_allow_html=True,
        )

    elif current == "half" and half:

        st.markdown(
            f"""
<img
class="envelope"
src="data:image/png;base64,{half}">
""",
            unsafe_allow_html=True,
        )

    st.markdown(
        """
<div class="message">

❤️

Every word inside this envelope
comes straight from my heart.

Will you open it?

❤️

</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # OPEN LETTER BUTTON
    # =====================================================

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        open_letter = st.button(
            "💌 Open My Letter ❤️",
            use_container_width=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # FLOATING HEARTS
    # =====================================================

    st.markdown(
        """
<style>

.heart{

position:fixed;

bottom:-80px;

font-size:26px;

animation:hearts 12s linear infinite;

pointer-events:none;

opacity:.8;

}

@keyframes hearts{

0%{
transform:translateY(0px) rotate(0deg);
opacity:0;
}

10%{
opacity:1;
}

100%{
transform:translateY(-120vh) rotate(360deg);
opacity:0;
}

}

</style>

<div class="heart" style="left:5%;animation-delay:0s;">❤️</div>
<div class="heart" style="left:18%;animation-delay:2s;">💕</div>
<div class="heart" style="left:33%;animation-delay:5s;">💖</div>
<div class="heart" style="left:51%;animation-delay:3s;">❤️</div>
<div class="heart" style="left:67%;animation-delay:6s;">💗</div>
<div class="heart" style="left:84%;animation-delay:1s;">💝</div>

""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # SPARKLES
    # =====================================================

    if sparkles:

        st.markdown(
            f"""
<img
src="data:image/png;base64,{sparkles}"
style="
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
opacity:.45;
pointer-events:none;
z-index:0;
">
""",
            unsafe_allow_html=True,
        )

    # =====================================================
    # PETALS
    # =====================================================

    if petals:

        st.markdown(
            f"""
<img
src="data:image/png;base64,{petals}"
style="
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
opacity:.35;
pointer-events:none;
animation:float 8s infinite;
z-index:0;
">
""",
            unsafe_allow_html=True,
        )

    # =====================================================
    # ENVELOPE REVEAL SEQUENCE
    # =====================================================

    if open_letter:

        placeholder = st.empty()

        # Step 1
        st.session_state.envelope_state = "opened"
        placeholder.success("💌 Opening the envelope...")
        st.rerun()

    # =====================================================
    # AUTO CONTINUE
    # =====================================================

    if st.session_state.envelope_state == "opened":

        import time

        time.sleep(1.2)

        st.session_state.envelope_state = "half"

        st.rerun()

    elif st.session_state.envelope_state == "half":

        import time

        time.sleep(1.5)

        st.success("❤️ Your letter is ready...")

        time.sleep(1)

        st.session_state.page = "letter"

        st.session_state.envelope_state = "closed"

        st.rerun()
