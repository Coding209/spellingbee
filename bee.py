import streamlit as st
import random

# Define word lists for each grade
word_lists = {
    "Grade1": ["apple", "ball", "cat", "dog", "egg"],
    "Grade2": ["banana", "clock", "dance", "eagle", "frog"],
    "Grade3": ["grape", "house", "island", "jungle", "kite"],
    "Grade4": ["lemon", "mountain", "needle", "orange", "piano"],
    "Grade5": ["quilt", "rocket", "sunshine", "tiger", "umbrella"],
}

# Initialize state to track used words
if "used_words" not in st.session_state:
    st.session_state["used_words"] = {grade: [] for grade in word_lists.keys()}

# Streamlit app title
st.title("Spelling Bee Word Picker")

# Select grade
selected_grade = st.selectbox("Select Grade:", options=list(word_lists.keys()))

# Pick a word button
if st.button("Pick a Word"):
    # Get available words for the selected grade
    available_words = [
        word for word in word_lists[selected_grade] 
        if word not in st.session_state["used_words"][selected_grade]
    ]

    # Check if there are words left
    if available_words:
        selected_word = random.choice(available_words)
        st.session_state["used_words"][selected_grade].append(selected_word)
        st.success(f"Selected Word: {selected_word}")
    else:
        st.warning("No more words available for this grade.")

# Reset words button
if st.button("Reset Words"):
    st.session_state["used_words"] = {grade: [] for grade in word_lists.keys()}
    st.info("All word lists have been reset.")
