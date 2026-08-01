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
# LETTER PAGE
# =====================================================

def letter_page():

    background = load_image(
        "assets/images/letter_background.png"
    )

    paper = load_image(
        "assets/images/letter_paper.png"
    )

    rose = load_image(
        "assets/images/rose.png"
    )

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

/* ----------------------------- */

@keyframes fade{

from{

opacity:0;
transform:translateY(50px);

}

to{

opacity:1;
transform:translateY(0px);

}

}

@keyframes floating{

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

/* ----------------------------- */

.title{

font-size:60px;

font-weight:800;

text-align:center;

color:white;

margin-top:35px;

text-shadow:4px 4px 18px black;

animation:fade 2s;

}

.subtitle{

font-size:22px;

text-align:center;

color:white;

margin-bottom:40px;

animation:fade 2.5s;

}

/* ----------------------------- */

.paper{

width:760px;

margin:auto;

padding:40px;

border-radius:30px;

background:rgba(255,255,255,.16);

backdrop-filter:blur(18px);

box-shadow:0 10px 35px rgba(0,0,0,.30);

border:1px solid rgba(255,255,255,.30);

animation:fade 2s;

}

/* ----------------------------- */

.paperImage{

display:block;

margin:auto;

width:500px;

animation:floating 5s infinite;

}

/* ----------------------------- */

.letter{

margin-top:20px;

font-size:22px;

line-height:40px;

color:#3c2c1f;

padding:40px;

height:520px;

overflow-y:auto;

border-radius:20px;

background:rgba(255,255,255,.45);

}

/* ----------------------------- */

.rose{

position:absolute;

top:80px;

right:120px;

width:120px;

}

/* ----------------------------- */

div.stButton > button{

height:60px;

font-size:22px;

font-weight:bold;

background:#D62839;

color:white;

border:none;

border-radius:18px;

}

div.stButton > button:hover{

background:#B00020;

transform:scale(1.03);

}

</style>
""",
        unsafe_allow_html=True,
    )

    # =====================================================

    st.markdown(
        """
<div class="title">

💌 A Letter Just For You

</div>

<div class="subtitle">

Some feelings cannot be spoken...

So I wrote them.

</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="paper">
""",
        unsafe_allow_html=True,
    )

    if paper:

        st.markdown(
            f"""
<img
class="paperImage"
src="data:image/png;base64,{paper}">
""",
            unsafe_allow_html=True,
        )

    st.markdown(
        """
<div class="letter">

<h2>Dear Chinnoda ❤️</h2>

<br>

<i>

Your beautiful love letter
will appear here...

</i>

<br><br><br>

❤️

</div>
""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # DECORATIVE ROSE
    # =====================================================

    if rose:

        st.markdown(
            f"""
<img
src="data:image/png;base64,{rose}"
style="
position:fixed;
top:80px;
right:60px;
width:140px;
z-index:999;
animation:floating 5s infinite;
">
""",
            unsafe_allow_html=True,
        )

    # =====================================================
    # SPARKLES
    # =====================================================

    sparkles = load_image(
        "assets/images/sparkles.png"
    )

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
pointer-events:none;
opacity:.45;
z-index:0;
">
""",
            unsafe_allow_html=True,
        )

    # =====================================================
    # PETALS
    # =====================================================

    petals = load_image(
        "assets/images/petals.png"
    )

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
pointer-events:none;
opacity:.35;
animation:floating 8s infinite;
z-index:0;
">
""",
            unsafe_allow_html=True,
        )

    # =====================================================
    # FLOATING HEARTS
    # =====================================================

    st.markdown(
        """
<style>

.heart{

position:fixed;

bottom:-80px;

font-size:28px;

animation:heartFloat 12s linear infinite;

opacity:.8;

pointer-events:none;

}

@keyframes heartFloat{

0%{

transform:translateY(0px) rotate(0deg);

opacity:0;

}

15%{

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
<div class="heart" style="left:32%;animation-delay:5s;">💖</div>
<div class="heart" style="left:48%;animation-delay:1s;">❤️</div>
<div class="heart" style="left:65%;animation-delay:6s;">💗</div>
<div class="heart" style="left:82%;animation-delay:3s;">💝</div>

""",
        unsafe_allow_html=True,
    )

    # =====================================================
    # AUDIO
    # =====================================================

    audio_file = "assets/audio/girlfriend_day.mp3"

    if Path(audio_file).exists():

        with open(audio_file, "rb") as audio:

            st.audio(audio.read(), autoplay=True)

    # =====================================================
    # CONTINUE BUTTON
    # =====================================================

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        continue_btn = st.button(
            "❤️ Continue ❤️",
            use_container_width=True,
        )

    # =====================================================
    # NAVIGATION
    # =====================================================

    if continue_btn:

        st.session_state.page = "finale"

        st.balloons()

        st.rerun()
