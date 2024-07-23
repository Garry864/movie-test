import streamlit as st

st.header("Watch movies here")


player = """
    <iframe frameborder="0" allowfullscreen="" scrolling="no" allow="autoplay;fullscreen" src="https://onelineplayer.com/player.html?autoplay=false&autopause=false&muted=false&loop=true&url=https%3A%2F%2Fwww.dropbox.com%2Fscl%2Ffi%2F8glj0g8vic3snmsp1tc92%2FSarileru-Neekevvaru-2022-Hindi-Dubbed-UnCut-720p-H.264-Vegamovies.to.mkv%3Frlkey%3Dbda2gv7cqc1lf8mld3myquqg9%26st%3Ds85etltb%26raw%3D1&poster=&time=true&progressBar=true&overlay=true&muteButton=true&fullscreenButton=true&style=light&quality=auto&playButton=true" style="height: 100%; width: 100%; aspect-ratio: 1280 / 544;"></iframe>
"""

st.markdown(player, unsafe_allow_html=True)