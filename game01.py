import streamlit as st
import random

# Initialize once
if "emojis" not in st.session_state:
    base_emojis = ["🐶", "🐱", "🦊", "🐻", "🐼", "🐨", "🐯", "🦁"]
    emoji_pairs = base_emojis * 2
    random.shuffle(emoji_pairs)
    st.session_state.emojis = emoji_pairs
    st.session_state.revealed = [False] * 16
    st.session_state.selected = []
    st.session_state.matched = []

# Layout
for row in range(4):
    cols = st.columns(4)
    for col in range(4):
        i = row * 4 + col
        if st.session_state.revealed[i] or i in st.session_state.matched:
            cols[col].button(st.session_state.emojis[i], key=f"btn{i}", disabled=True)
        else:
            if cols[col].button("❓", key=f"btn{i}"):
                st.session_state.revealed[i] = True
                st.session_state.selected.append(i)

# Matching logic
if len(st.session_state.selected) == 2:
    a, b = st.session_state.selected
    if st.session_state.emojis[a] == st.session_state.emojis[b]:
        st.session_state.matched.extend([a, b])
    else:
        st.session_state.revealed[a] = False
        st.session_state.revealed[b] = False
    st.session_state.selected = []

# Win check
if len(st.session_state.matched) == 16:
    st.balloons()
    st.success("🎉 You matched all pairs!")

# Reset button
if st.button("🔁 New Game"):
    random.shuffle(st.session_state.emojis)
    st.session_state.revealed = [False] * 16
    st.session_state.selected = []
    st.session_state.matched = []
