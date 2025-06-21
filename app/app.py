import time
import streamlit as st



prompt = st.chat_input("Ask a question...")

if prompt:

    with st.chat_message("user"):
        st.write(prompt)

    #######################################
    # Hands on activity
    # Make a request to OpenAI and visualize it using chat_message()


    with st.chat_message("ai"):
        st.write("LLM output goes here...")