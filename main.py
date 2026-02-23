import streamlit as st
import cohere

# Securely accessing the API Key
api_key = st.secrets["COHERE_API_KEY"]
co = cohere.Client(api_key)

# Page Configuration for a professional look
st.set_page_config(page_title="EduGenie AI", page_icon="🎓", layout="centered")

# Custom Sidebar with project details
with st.sidebar:
    st.title("🎓 Project Info")
    st.markdown("""
    **Project:** EduGenie - AI Study Buddy  
    **Domain:** Artificial Intelligence  
    **Internship:** IBM SkillsBuild / Edunet  
    """)
    st.divider()
    mode = st.radio(
        "Choose a Tool:",
        ["Simplify Concept", "Summarize Notes", "Generate Quiz"]
    )
    st.info("Select a mode and paste your text in the main window to begin.")

# Main Header
st.title("📚 EduGenie: Your AI Study Buddy")
st.write("This tool uses Generative AI to help students understand complex topics faster.")

# User Input Area
st.subheader(f"Current Tool: {mode}")
user_input = st.text_area("Paste your study material or topic below:", height=200, placeholder="e.g., Explain the concept of Data Structures...")

# Action Button
if st.button("Generate Result", use_container_width=True):
    if user_input:
        # Dynamic Prompting logic based on your PDF requirements
        if mode == "Simplify Concept":
            system_prompt = "You are a helpful tutor. Explain the following concept in simple, easy-to-understand language for a student."
        elif mode == "Summarize Notes":
            system_prompt = "You are an assistant. Summarize these notes into clear, organized bullet points."
        else:
            system_prompt = "You are a quiz master. Create a 3-question Multiple Choice Quiz with answers based on this text."

        with st.spinner("EduGenie is thinking..."):
            try:
                response = co.chat(
                    message=user_input,
                    preamble=system_prompt,
                    model="command-r-plus"
                )
                st.markdown("### ✨ Response")
                st.success("Analysis Complete!")
                st.write(response.text)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please provide some text or a topic to proceed.")

# Footer
st.divider()
st.caption("Developed as part of the IBM SkillsBuild AI/ML Internship - January 2026 Batch")
