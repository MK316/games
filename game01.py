import streamlit as st
import random

# Emoji pairs
emojis = ["🐶", "🐱", "🐶", "🐱"]
random.shuffle(emojis)

# Initialize game state
if "revealed" not in st.session_state:
    st.session_state.revealed = [False] * 4
    st.session_state.selected = []
    st.session_state.emojis = emojis.copy()
    st.session_state.matched = []

# Layout
cols = st.columns(4)
for i in range(4):
    if st.session_state.revealed[i] or i in st.session_state.matched:
        cols[i].button(st.session_state.emojis[i], key=f"btn{i}", disabled=True)
    else:
        if cols[i].button("❓", key=f"btn{i}"):
            st.session_state.revealed[i] = True
            st.session_state.selected.append(i)

# Matching logic
if len(st.session_state.selected) == 2:
    a, b = st.session_state.selected
    if st.session_state.emojis[a] == st.session_state.emojis[b]:
        st.session_state.matched += [a, b]
    else:
        st.session_state.revealed[a] = False
        st.session_state.revealed[b] = False
    st.session_state.selected = []

# Check win
if len(st.session_state.matched) == len(st.session_state.emojis):
    st.balloons()
    st.success("🎉 Congratulations! You matched all pairs!")

# New game button
if st.button("🔁 New Game"):
    random.shuffle(st.session_state.emojis)
    st.session_state.revealed = [False] * 4
    st.session_state.selected = []
    st.session_state.matched = []
