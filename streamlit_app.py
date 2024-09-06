# streamlit_word_count.py

import streamlit as st

# Title of the app
st.title("Word Count App")

# Add a description
st.write("This app counts the number of words in the text entered by the user.")

# Input text from the user
user_input = st.text_area("Enter some text:")

# Button to trigger word count
if st.button("Count Words"):
    # Split the input text by spaces and count words
    word_count = len(user_input.split())
    
    # Display the word count
    st.write(f"Word Count: {word_count}")
else:
    st.write("Enter text and click the button to count the words.")



