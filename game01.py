import streamlit as st
import random

# Sample word-meaning pairs
pairs = {
    "benevolent": "kind and generous",
    "ambiguous": "unclear or doubtful",
    "resilient": "able to recover quickly",
    "eloquent": "fluent or persuasive in speaking"
}

words = list(pairs.keys())
meanings = list(pairs.values())

# Shuffle meanings for matching interface
if "shuffled_meanings" not in st.session_state:
    st.session_state.shuffled_meanings = random.sample(meanings, len(meanings))
if "selections" not in st.session_state:
    st.session_state.selections = [None] * len(words)

st.markdown("### ✏️ Match the words with their meanings")

# Create matching interface
for i, word in enumerate(words):
    cols = st.columns([1, 2])
    cols[0].markdown(f"**{word}**")
    st.session_state.selections[i] = cols[1].selectbox(
        f"Select meaning for '{word}'", 
        options=["-- Choose --"] + st.session_state.shuffled_meanings,
        key=f"select_{i}"
    )

# Show result button
if st.button("✅ Show Result"):
    correct = 0
    for i, word in enumerate(words):
        selected = st.session_state.selections[i]
        if selected == pairs[word]:
            st.success(f"✔️ Correct match for **{word}**")
            correct += 1
        else:
            st.error(f"❌ Incorrect match for **{word}**")

    if correct == len(words):
        st.balloons()
        st.success("🎉 All matches are correct! Well done!")
    else:
        st.info(f"You got {correct} out of {len(words)} correct.")

# Reset game
if st.button("🔁 Try Again"):
    st.session_state.shuffled_meanings = random.sample(meanings, len(meanings))
    st.session_state.selections = [None] * len(words)
