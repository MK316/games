import streamlit as st
import random

# Hangman stages (6 attempts max)
HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

# Word list
WORDS = ["banana", "hangman", "streamlit", "elephant", "python", "emoji"]

# Initialize session state
if "word" not in st.session_state:
    st.session_state.word = random.choice(WORDS)
    st.session_state.guessed = []
    st.session_state.wrong = 0
    st.session_state.game_over = False

# Display title
st.title("🎯 Hangman Game")

# Display hangman figure
st.text(HANGMAN_PICS[st.session_state.wrong])

# Display current word progress
display_word = " ".join([letter if letter in st.session_state.guessed else "_" for letter in st.session_state.word])
st.markdown(f"### Word: {display_word}")

# User input
if not st.session_state.game_over:
    guess = st.text_input("Guess a letter", max_chars=1)

    if guess:
        guess = guess.lower()

        if guess in st.session_state.guessed:
            st.warning("You've already guessed that letter.")
        elif guess in st.session_state.word:
            st.session_state.guessed.append(guess)
            st.success(f"✅ Correct! `{guess}` is in the word.")
        else:
            st.session_state.guessed.append(guess)
            st.session_state.wrong += 1
            st.error(f"❌ Wrong guess! `{guess}` is not in the word.")

    # Check win
    if all(letter in st.session_state.guessed for letter in st.session_state.word):
        st.success(f"🎉 Congratulations! You guessed the word: **{st.session_state.word}**")
        st.balloons()
        st.session_state.game_over = True

    # Check loss
    if st.session_state.wrong == len(HANGMAN_PICS) - 1:
        st.error(f"💀 Game Over! The word was: **{st.session_state.word}**")
        st.session_state.game_over = True

# New game button
if st.button("🔁 Play Again"):
    st.session_state.word = random.choice(WORDS)
    st.session_state.guessed = []
    st.session_state.wrong = 0
    st.session_state.game_over = False
