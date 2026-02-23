import streamlit as st
import cohere

co = cohere.Client("YOUR_COHERE_API_KEY")

st.set_page_config(page_title="EduGenie", page_icon="📖")
st.title("EduGenie: AI Study Buddy")

mode = st.sidebar.selectbox(
    "Select Action:",
    ["Simplify Concept", "Summarize Notes", "Generate Quiz"]
)

if mode == "Simplify Concept":
    system_prompt = "Explain this topic in very simple terms for a student."
elif mode == "Summarize Notes":
    system_prompt = "Summarize the following notes into clear bullet points."
else:
    system_prompt = "Create a 3-question MCQ quiz based on this text."

user_input = st.text_area("Enter your topic or notes here:")

if st.button("Start"):
    if user_input:
        with st.spinner("Processing..."):
            response = co.chat(
                message=user_input,
                preamble=system_prompt,
                model="command-r-plus"
            )
            st.success("Done!")
            st.write(response.text)
    else:
        st.warning("Please enter some text first.")
