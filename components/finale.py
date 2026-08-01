import streamlit as st
import base64
from pathlib import Path


# ==========================================================
# IMAGE LOADER
# ==========================================================

def load_image(path):

    file = Path(path)

    if not file.exists():
        return None

    return base64.b64encode(file.read_bytes()).decode()


# ==========================================================
# FINALE PAGE
# ==========================================================

def finale_page():

    background = load_image(
        "assets/images/letter_background.png"
    )

    # ------------------------------------------------------

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

    # ------------------------------------------------------

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

@keyframes glow{

0%{

text-shadow:0 0 10px rgba(255,255,255,.3);

}

50%{

text-shadow:0 0 30px rgba(255,255,255,.9);

}

100%{

text-shadow:0 0 10px rgba(255,255,255,.3);

}

}

@keyframes floating{

0%{

transform:translateY(0px);

}

50%{

transform:translateY(-10px);

}

100%{

transform:translateY(0px);

}

}

.title{

font-size:72px;

font-weight:800;

text-align:center;

margin-top:80px;

color:white;

animation:fade 2s, glow 3s infinite;

}

.message{

margin:auto;

width:900px;

margin-top:60px;

padding:50px;

border-radius:30px;

background:rgba(255,255,255,.16);

backdrop-filter:blur(20px);

box-shadow:0 12px 40px rgba(0,0,0,.35);

color:white;

font-size:30px;

line-height:55px;

text-align:center;

animation:fade 2.5s;

}

.signature{

margin-top:70px;

text-align:center;

font-size:34px;

color:white;

animation:floating 5s infinite;

}

div.stButton>button{

height:60px;

font-size:22px;

border-radius:18px;

font-weight:bold;

background:#d62839;

color:white;

border:none;

}

div.stButton>button:hover{

background:#b00020;

transform:scale(1.03);

}

</style>
""",
        unsafe_allow_html=True,
    )

    # ------------------------------------------------------

    st.markdown(
        """
<div class="title">

❤️ Happy National Girlfriend Day ❤️

</div>

<div class="message">

Every flower eventually fades...

Every season eventually changes...

But one thing that will never change...

is the place you hold in my heart.

🌹

Thank you for being the most beautiful
part of my life.

❤️

</div>

<div class="signature">

Forever Yours ❤️

</div>

""",
        unsafe_allow_html=True,
    )

    # ==========================================================
    # LOAD DECORATIVE ASSETS
    # ==========================================================

    petals = load_image(
        "assets/images/petals.png"
    )

    sparkles = load_image(
        "assets/images/sparkles.png"
    )

    # ==========================================================
    # SPARKLES
    # ==========================================================

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

    # ==========================================================
    # PETALS
    # ==========================================================

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

    # ==========================================================
    # FLOATING HEARTS
    # ==========================================================

    st.markdown(
        """
<style>

.heart{

position:fixed;

bottom:-80px;

font-size:28px;

animation:heartFloat 12s linear infinite;

pointer-events:none;

opacity:.85;

}

@keyframes heartFloat{

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
<div class="heart" style="left:32%;animation-delay:5s;">💖</div>
<div class="heart" style="left:48%;animation-delay:1s;">❤️</div>
<div class="heart" style="left:65%;animation-delay:6s;">💗</div>
<div class="heart" style="left:82%;animation-delay:3s;">💝</div>

""",
        unsafe_allow_html=True,
    )

    # ==========================================================
    # BALLOONS
    # ==========================================================

    if "finale_once" not in st.session_state:

        st.session_state.finale_once = True

        st.balloons()

    # ==========================================================
    # THANK YOU
    # ==========================================================

    st.write("")
    st.write("")

    st.markdown(
        """
<div style="
text-align:center;
font-size:20px;
color:white;
opacity:.9;
margin-top:20px;
">

🌹

Thank you for reading my little surprise.

I hope it made you smile.

❤️

</div>
""",
        unsafe_allow_html=True,
    )

    # ==========================================================
    # FINISH BUTTON
    # ==========================================================

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        if st.button(
            "❤️ The End ❤️",
            use_container_width=True,
        ):

            st.success("Happy National Girlfriend Day ❤️")
