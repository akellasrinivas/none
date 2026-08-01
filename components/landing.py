import streamlit as st
import base64
from pathlib import Path


# ---------------------------------------------------
# Helper
# ---------------------------------------------------

def get_base64(path):
    file = Path(path)

    if not file.exists():
        return None

    return base64.b64encode(file.read_bytes()).decode()


# ---------------------------------------------------
# Landing Page
# ---------------------------------------------------

def landing_page():

    background = get_base64("assets/images/landing_background.png")
    bouquet = get_base64("assets/images/bouquet_box.png")

    # --------------------------------------------
    # Background
    # --------------------------------------------

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
            overflow:hidden;
        }}

        </style>
        """,
            unsafe_allow_html=True,
        )

    # --------------------------------------------
    # CSS
    # --------------------------------------------

    st.markdown(
        """
<style>

.main > div{
padding-top:0rem;
}

/* Hide Streamlit */

header{
visibility:hidden;
}

footer{
visibility:hidden;
}

#MainMenu{
visibility:hidden;
}


/* Floating animation */

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

/* Fade */

@keyframes fade{

from{
opacity:0;
transform:translateY(40px);
}

to{

opacity:1;
transform:translateY(0px);

}

}


/* Glow */

@keyframes glow{

0%{
box-shadow:0 0 15px rgba(255,255,255,.3);
}

50%{
box-shadow:0 0 40px rgba(255,255,255,.8);
}

100%{
box-shadow:0 0 15px rgba(255,255,255,.3);
}

}


/* Heading */

.bigTitle{

font-size:65px;

font-weight:800;

text-align:center;

margin-top:30px;

color:white;

text-shadow:4px 4px 20px black;

animation:fade 2s ease;

}


/* Subtitle */

.subtitle{

font-size:24px;

text-align:center;

color:white;

margin-bottom:60px;

animation:fade 2.5s ease;

}


/* Gift Card */

.giftCard{

width:700px;

margin:auto;

padding:35px;

border-radius:25px;

background:rgba(255,255,255,.15);

backdrop-filter:blur(18px);

border:1px solid rgba(255,255,255,.35);

box-shadow:0 10px 40px rgba(0,0,0,.35);

animation:fade 2s ease;

}


/* Gift Image */

.giftImage{

display:block;

margin:auto;

width:350px;

animation:float 5s infinite;

}


/* Quote */

.quote{

font-size:22px;

text-align:center;

color:white;

margin-top:25px;

line-height:40px;

}


/* Button */

div.stButton>button{

background:#D62839;

color:white;

height:60px;

font-size:24px;

border-radius:18px;

font-weight:bold;

border:none;

transition:.3s;

animation:glow 2s infinite;

}


div.stButton>button:hover{

transform:scale(1.03);

background:#B00020;

}

</style>

""",
        unsafe_allow_html=True,
    )

    # ----------------------------------------
    # Title
    # ----------------------------------------

    st.markdown(
        """
<div class="bigTitle">

❤️ Happy National Girlfriend Day ❤️

</div>

<div class="subtitle">

Every beautiful love story deserves
a beautiful surprise...

</div>

""",
        unsafe_allow_html=True,
    )

    # ----------------------------------------
    # Card
    # ----------------------------------------

    st.markdown(
        """
<div class="giftCard">
""",
        unsafe_allow_html=True,
    )

    if bouquet:

        st.markdown(
            f"""
<img class="giftImage"
src="data:image/png;base64,{bouquet}">
""",
            unsafe_allow_html=True,
        )

    st.markdown(
        """
<div class="quote">

🌹

A little surprise...
wrapped with love,
made especially for you.

🌹

</div>

""",
        unsafe_allow_html=True,
    )


    # ----------------------------------------
    # Decorative Header
    # ----------------------------------------

    st.markdown(
        """
        <div style="
            text-align:center;
            color:white;
            font-size:20px;
            margin-top:25px;
            margin-bottom:10px;
        ">
            ✨ Made with love... Just for You ✨
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ----------------------------------------
    # Open Surprise Button
    # ----------------------------------------

    st.write("")
    st.write("")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:

        open_surprise = st.button(
            "🎁 Open My Surprise ❤️",
            use_container_width=True,
        )

    st.write("")
    st.write("")

    # ----------------------------------------
    # Romantic Footer
    # ----------------------------------------

    st.markdown(
        """
        <div style="
            text-align:center;
            color:white;
            font-size:18px;
            opacity:0.9;
            line-height:35px;
        ">

        ❤️

        Every flower has a fragrance...
        Every star has its light...

        But my favorite part of this world...

        is YOU.

        ❤️

        </div>
        """,
        unsafe_allow_html=True,
    )

    # Close Gift Card
    st.markdown("</div>", unsafe_allow_html=True)

    # ----------------------------------------
    # Floating Hearts Overlay
    # ----------------------------------------

    st.markdown(
        """
        <style>

        .heart{

            position:fixed;
            bottom:-60px;

            color:#ff4d6d;

            font-size:25px;

            animation:floatHeart 12s linear infinite;

            opacity:.7;

            pointer-events:none;

        }

        @keyframes floatHeart{

            0%{
                transform:translateY(0) rotate(0deg);
                opacity:0;
            }

            10%{
                opacity:1;
            }

            100%{
                transform:translateY(-110vh) rotate(360deg);
                opacity:0;
            }

        }

        </style>

        <div class="heart" style="left:8%; animation-delay:0s;">❤️</div>
        <div class="heart" style="left:22%; animation-delay:2s;">💖</div>
        <div class="heart" style="left:38%; animation-delay:5s;">💕</div>
        <div class="heart" style="left:55%; animation-delay:3s;">❤️</div>
        <div class="heart" style="left:73%; animation-delay:7s;">💗</div>
        <div class="heart" style="left:88%; animation-delay:1s;">💝</div>

        """,
        unsafe_allow_html=True,
    )

    # ----------------------------------------
    # Navigation
    # ----------------------------------------

    if open_surprise:

        st.session_state.page = "giftbox"

        st.success("❤️ Opening your surprise...")

        st.balloons()

        st.rerun()
