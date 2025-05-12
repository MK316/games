import streamlit as st
import random

# Hangman stages (6 wrong guesses allowed)
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

# Word list with hints
WORDS = {
    "banana": "a yellow fruit",
    "streamlit": "Python tool to build web apps",
    "elephant": "the largest land animal",
    "python": "a programming language or a snake",
    "umbrella": "used in rain",
    "hangman": "a classic word guessing game"
}

# Initialize game state safely
if "word" not in st.session_state:
    st.session_state.word = random.choice(list(WORDS.keys()))
    st.session_state.hint = WORDS[st.session_state.word]
    st.session_state.guessed = []
    st.session_state.wrong = 0
    st.session_state.game_over = False

# Ensure 'hint' is always initialized
if "hint" not in st.session_state:
    st.session_state.hint = WORDS[st.session_state.word]


# Display game title and hint
st.title("🎯 Hangman with Hints")
st.markdown(f"💡 **Hint**: *{st.session_state.hint}*")

# Show hangman drawing
st.text(HANGMAN_PICS[min(st.session_state.wrong, len(HANGMAN_PICS) - 1)])


# Show word progress
display_word = " ".join([letter if i < len(st.session_state.guessed) else "_" for i, letter in enumerate(st.session_state.word)])
st.markdown(f"### Word: {display_word}")

MAX_WRONG = len(HANGMAN_PICS) - 1

    if not st.session_state.game_over and st.session_state.wrong < MAX_WRONG:


# Display feedback after rerun
if "feedback" in st.session_state:
    if st.session_state.feedback_type == "success":
        st.success(st.session_state.feedback)
    elif st.session_state.feedback_type == "error":
        st.error(st.session_state.feedback)



# Win condition
if len(st.session_state.guessed) == len(st.session_state.word):
    st.success(f"🎉 You spelled the word correctly: **{st.session_state.word}**")
    st.balloons()
    st.session_state.game_over = True

# Lose condition
if st.session_state.wrong == len(HANGMAN_PICS) - 1:
    st.error(f"💀 Game Over! The correct word was: **{st.session_state.word}**")
    st.session_state.game_over = True

# Play again button
if st.button("🔁 Play Again"):
    st.session_state.word = random.choice(list(WORDS.keys()))
    st.session_state.hint = WORDS[st.session_state.word]
    st.session_state.guessed = []
    st.session_state.wrong = 0
    st.session_state.game_over = False
