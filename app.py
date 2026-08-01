import streamlit as st
from pathlib import Path
import base64

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Happy National Girlfriend Day ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================================
# IMPORT COMPONENTS
# ==========================================================

from components.login import login_page
from components.landing import landing_page
from components.giftbox import giftbox_page
from components.envelope import envelope_page
from components.letter import letter_page
from components.finale import finale_page

# ==========================================================
# LOAD CSS FILES
# ==========================================================

def load_css(file_path):

    css_file = Path(file_path)

    if css_file.exists():

        with open(css_file) as f:

            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True,
            )

# Load Global CSS
load_css("styles/style.css")

# Load Animation CSS
load_css("styles/animations.css")

# ==========================================================
# SESSION STATE INITIALIZATION
# ==========================================================

default_states = {

    "authenticated": False,

    "page": "login",

    "envelope_state": "closed",

    "gift_opened": False,

    "letter_opened": False,

    "finale_once": False,

}

for key, value in default_states.items():

    if key not in st.session_state:

        st.session_state[key] = value

# ==========================================================
# HELPER FUNCTIONS
# ==========================================================

def reset_story():
    """
    Reset the complete story.
    """

    st.session_state.authenticated = False

    st.session_state.page = "login"

    st.session_state.envelope_state = "closed"

    st.session_state.gift_opened = False

    st.session_state.letter_opened = False

    st.session_state.finale_once = False


def page_title():

    st.markdown(
        """
        <div style="
        text-align:center;
        color:white;
        font-size:18px;
        margin-top:-15px;
        margin-bottom:20px;
        opacity:.8;
        ">
        Made with ❤️
        </div>
        """,
        unsafe_allow_html=True,
    )


def show_loading(text):

    with st.spinner(text):

        pass


# ==========================================================
# ROUTING FUNCTION
# ==========================================================

def router():

    page = st.session_state.page

    # LOGIN

    if page == "login":

        login_page()

        return

    # Prevent bypassing login

    if not st.session_state.authenticated:

        st.session_state.page = "login"

        st.rerun()

    # LANDING

    if page == "landing":

        landing_page()

        return

    # GIFT BOX

    if page == "giftbox":

        giftbox_page()

        return

    # ==========================================================
    # ENVELOPE
    # ==========================================================

    elif page == "envelope":

        envelope_page()

        return

    # ==========================================================
    # LETTER
    # ==========================================================

    elif page == "letter":

        letter_page()

        return

    # ==========================================================
    # FINALE
    # ==========================================================

    elif page == "finale":

        finale_page()

        return

    # ==========================================================
    # UNKNOWN PAGE
    # ==========================================================

    else:

        st.warning("Unknown page detected. Redirecting...")

        st.session_state.page = "login"

        st.rerun()


# ==========================================================
# MAIN APPLICATION
# ==========================================================

def main():

    try:

        router()

    except Exception as e:

        st.error("Something went wrong.")

        with st.expander("Developer Error"):

            st.exception(e)

        col1, col2, col3 = st.columns([1,2,1])

        with col2:

            if st.button(
                "🔄 Restart Story",
                use_container_width=True
            ):

                reset_story()

                st.rerun()


# ==========================================================
# RUN APPLICATION
# ==========================================================

if __name__ == "__main__":

    main()
  
