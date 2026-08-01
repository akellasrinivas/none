# components/login.py

import streamlit as st
import base64
from pathlib import Path


PASSWORD = "chinnoda"


def _image_to_base64(path: str):
    """Convert image to base64 for CSS background."""
    img_path = Path(path)
    if not img_path.exists():
        return None

    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def login_page():
    """
    Romantic Login Screen
    Returns True when authenticated.
    """

    bg = _image_to_base64("assets/images/landing_background.png")

    if bg:
        background_css = f"""
        <style>

        .stApp {{
            background-image:url("data:image/png;base64,{bg}");
            background-size:cover;
            background-position:center;
            background-repeat:no-repeat;
            background-attachment:fixed;
        }}

        </style>
        """
    else:
        background_css = """
        <style>

        .stApp{
            background:linear-gradient(135deg,#ffdde1,#ee9ca7);
        }

        </style>
        """

    st.markdown(background_css, unsafe_allow_html=True)

    st.markdown(
        """
        <style>

        .main > div{
            padding-top:0rem;
        }

        div[data-testid="stVerticalBlock"]{
            gap:0.6rem;
        }

        .title{
            text-align:center;
            color:white;
            font-size:54px;
            font-weight:700;
            margin-top:40px;
            text-shadow:2px 2px 12px rgba(0,0,0,0.35);
        }

        .subtitle{
            text-align:center;
            color:white;
            font-size:22px;
            margin-bottom:30px;
        }

        .glass{

            width:480px;
            margin:auto;
            margin-top:40px;

            padding:35px;

            border-radius:25px;

            backdrop-filter:blur(18px);

            background:rgba(255,255,255,.15);

            border:1px solid rgba(255,255,255,.30);

            box-shadow:
                0 8px 40px rgba(0,0,0,.35);

        }

        .quote{
            color:white;
            text-align:center;
            font-size:18px;
            margin-bottom:25px;
            font-style:italic;
        }

        div[data-testid="stTextInput"] input{

            border-radius:15px;
            height:55px;
            font-size:18px;
            border:none;

        }

        div.stButton>button{

            width:100%;
            height:55px;

            border-radius:16px;

            background:#E63946;
            color:white;

            font-size:20px;
            font-weight:bold;

            border:none;

            transition:.3s;

        }

        div.stButton>button:hover{

            background:#C1121F;
            transform:scale(1.02);

        }

        .footer{

            text-align:center;
            color:white;
            margin-top:30px;
            font-size:15px;
            opacity:.8;

        }

        </style>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="title">
            ❤️ National Girlfriend Day ❤️
        </div>

        <div class="subtitle">
            A little surprise is waiting just for you...
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.container():

        st.markdown('<div class="glass">', unsafe_allow_html=True)

        st.markdown(
            """
            <div class="quote">
            "Some gifts are wrapped in paper...
            the best ones are wrapped in love."
            </div>
            """,
            unsafe_allow_html=True,
        )

        password = st.text_input(
            "Enter Secret Password",
            type="password",
            placeholder="Type here...",
            label_visibility="visible",
        )

        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:

            unlock = st.button(
                "🔓 Unlock My Heart",
                use_container_width=True,
            )

        st.markdown("</div>", unsafe_allow_html=True)

    if unlock:

        if password.strip().lower() == PASSWORD.lower():

            st.session_state.authenticated = True
            st.session_state.page = "landing"

            st.success("❤️ Welcome Chinnoda ❤️")

            st.balloons()

            st.rerun()

        else:

            st.error("💔 Wrong password. This surprise belongs to someone very special.")

    st.markdown(
        """
        <div class="footer">
            Made with ❤️ exclusively for one special person
        </div>
        """,
        unsafe_allow_html=True,
    )
