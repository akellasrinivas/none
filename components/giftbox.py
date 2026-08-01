import streamlit as st
import base64
from pathlib import Path
import time


# ----------------------------------------------------------
# IMAGE LOADER
# ----------------------------------------------------------

def load_image(path):

    file = Path(path)

    if not file.exists():
        return None

    return base64.b64encode(file.read_bytes()).decode()


# ----------------------------------------------------------
# GIFT BOX PAGE
# ----------------------------------------------------------

def giftbox_page():

    background = load_image(
        "assets/images/landing_background.png"
    )

    gift = load_image(
        "assets/images/bouquet_box.png"
    )

    petals = load_image(
        "assets/images/petals.png"
    )

    sparkles = load_image(
        "assets/images/sparkles.png"
    )

    # ----------------------------------------------------------

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

    # ----------------------------------------------------------

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

.main>div{
padding-top:0rem;
}

/* ------------------------------------------------ */

@keyframes fade{

from{

opacity:0;
transform:translateY(50px);

}

to{

opacity:1;
transform:translateY(0);

}

}

@keyframes floating{

0%{

transform:translateY(0px);

}

50%{

transform:translateY(-15px);

}

100%{

transform:translateY(0px);

}

}

@keyframes pulse{

0%{

transform:scale(1);

}

50%{

transform:scale(1.03);

}

100%{

transform:scale(1);

}

}

/* ------------------------------------------------ */

.title{

font-size:60px;

color:white;

font-weight:800;

text-align:center;

margin-top:40px;

text-shadow:3px 3px 18px black;

animation:fade 2s;

}

.subtitle{

font-size:22px;

color:white;

text-align:center;

margin-bottom:50px;

animation:fade 2.5s;

}

.card{

width:760px;

margin:auto;

padding:40px;

border-radius:30px;

background:rgba(255,255,255,.18);

backdrop-filter:blur(20px);

border:1px solid rgba(255,255,255,.30);

box-shadow:0 12px 35px rgba(0,0,0,.35);

animation:fade 2s;

}

.gift{

width:380px;

display:block;

margin:auto;

animation:floating 5s infinite;

}

.quote{

color:white;

text-align:center;

font-size:22px;

line-height:40px;

margin-top:30px;

}

</style>
""",
        unsafe_allow_html=True,
    )

    # ----------------------------------------------------------

    st.markdown(
        """
<div class="title">

🎁 Your Surprise Awaits

</div>

<div class="subtitle">

Some gifts carry flowers...

Some gifts carry feelings...

This one carries both.

</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="card">
""",
        unsafe_allow_html=True,
    )

    if gift:

        st.markdown(
            f"""
<img class="gift"
src="data:image/png;base64,{gift}">
""",
            unsafe_allow_html=True,
        )

    st.markdown(
        """
<div class="quote">

🌹

Every petal reminds me of you.

Every flower blooms because
you exist in my life.

🌹

</div>
""",
        unsafe_allow_html=True,
    )

    # ----------------------------------------------------------
    # Decorative Divider
    # ----------------------------------------------------------

    st.markdown(
        """
        <div style="
            text-align:center;
            color:white;
            font-size:22px;
            margin-top:25px;
            margin-bottom:30px;
        ">
            ✨ A little token of my love ✨
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ----------------------------------------------------------
    # OPEN GIFT BUTTON
    # ----------------------------------------------------------

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        open_gift = st.button(
            "🎁 Open The Gift ❤️",
            use_container_width=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # ----------------------------------------------------------
    # FLOATING HEARTS
    # ----------------------------------------------------------

    st.markdown(
        """
<style>

.heart{

position:fixed;

bottom:-50px;

font-size:24px;

animation:heartFloat 12s linear infinite;

pointer-events:none;

opacity:.8;

}

@keyframes heartFloat{

0%{
transform:translateY(0) rotate(0deg);
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

<div class="heart" style="left:8%; animation-delay:0s;">❤️</div>
<div class="heart" style="left:20%; animation-delay:4s;">💕</div>
<div class="heart" style="left:37%; animation-delay:1s;">💖</div>
<div class="heart" style="left:55%; animation-delay:6s;">❤️</div>
<div class="heart" style="left:72%; animation-delay:3s;">💗</div>
<div class="heart" style="left:88%; animation-delay:5s;">💝</div>

""",
        unsafe_allow_html=True,
    )

    # ----------------------------------------------------------
    # SPARKLE OVERLAY
    # ----------------------------------------------------------

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

    # ----------------------------------------------------------
    # PETAL OVERLAY
    # ----------------------------------------------------------

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
z-index:0;
animation:floating 8s infinite;
">
""",
            unsafe_allow_html=True,
        )

    # ----------------------------------------------------------
    # BUTTON ACTION
    # ----------------------------------------------------------

    if open_gift:

        placeholder = st.empty()

        placeholder.success("🎀 Opening your gift...")

        time.sleep(1)

        placeholder.success("🌹 The bouquet blooms beautifully...")

        time.sleep(1.5)

        placeholder.success("💌 There's something hidden behind it...")

        time.sleep(1.5)

        placeholder.empty()

        st.balloons()

        st.session_state.page = "envelope"

        st.rerun()
