import streamlit as st

st.title("My First Streamlit app 🚀")


with st.sidebar:
    
    st.header("Button")
    st.button("My button")
    
    st.divider()
    st.header("Checkbox")
    st.checkbox(label="LLM")
    
    st.divider()
    st.header("Multiselect")
    st.multiselect(label="Language Models", options=["GPT-4o", "Gemini 2.5", "Llamba", "Claude"])

    st.divider()
    st.header("Radio")
    genre = st.radio(
    "What's your favorite movie genre",
    ["**Comedy**", "***Drama***", "Documentary :movie_camera:"],
    captions=[
        "Laugh out loud.",
        "Get the popcorn.",
        "Never stop learning.",
    ])


    st.divider()
    st.header("Slider")
    color = st.select_slider(
    "Select a color of the rainbow",
    options=[
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet",
    ])


    st.divider()
    st.header("Slider with Numbers")
    st.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))


prompt = st.chat_input("Ask a question 🤗")
if prompt:

    with st.chat_message("user"):
        st.write(f"{prompt}")

