import streamlit as st
from langchain_ollama import OllamaLLM
import PyPDF2
import requests
import time

# Initialize the model
model = OllamaLLM(model="llama3.1:8b")

# Set the page configuration
st.set_page_config(page_title="Text Summarization App", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f5;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: None;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar for settings
st.sidebar.header("Settings")
temperature = st.sidebar.slider("Select temperature:", min_value=0.0, max_value=1.0, value=0.5)
summary_style = st.sidebar.selectbox("Select summary style:", ["Extractive", "Abstractive"])
keyword_focus = st.sidebar.text_input("Enter keywords to focus on (optional):")

# Title and description
st.title("📝 Text Summarization App")
st.markdown("""
    This app allows you to summarize text from various sources including direct text input, PDF files, and URLs.
    Customize your summarization with options for word limit, temperature, summary style, and keyword focus.
    You can also try the sample inputs below to see how it works!
""")

# Sample inputs for demonstration
st.markdown("### Sample Inputs")
st.markdown("**Text Input:** `This is a sample text that can be summarized.`")
st.markdown("**PDF Input:** Upload a PDF file containing text.")
st.markdown("**URL Input:** `https://example.com/sample-article`")

# Input type selection
input_type = st.selectbox("Select input type:", ["Text", "PDF", "URL"])

# Create a container for inputs
with st.container():
    if input_type == "Text":
        user_input = st.text_area("Enter text to summarize:", height=200)
    elif input_type == "PDF":
        uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
        if uploaded_file is not None:
            reader = PyPDF2.PdfReader(uploaded_file)
            user_input = " ".join(page.extract_text() for page in reader.pages if page.extract_text())
    elif input_type == "URL":
        url = st.text_input("Enter URL to summarize:")
        if url:
            response = requests.get(url)
            user_input = response.text
    else:
        user_input = ""

    # Word limit inputs
    min_word_limit = st.number_input("Enter minimum word limit for summary:", min_value=1, value=50)
    max_word_limit = st.number_input("Enter maximum word limit for summary:", min_value=1, value=100)

    # Button to generate summary
    if st.button("Generate Summary"):
        if user_input:
            with st.spinner("Generating summary..."):
                time.sleep(2)  # Simulate processing time
                prompt = f"Summarize the following text to between {min_word_limit} and {max_word_limit} words with a temperature of {temperature}, using {summary_style} summarization."
                if keyword_focus:
                    prompt += f" Focus on the following keywords: {keyword_focus}"
                prompt += f" Text: {user_input}"
                
                response = model.invoke(prompt)
                st.subheader("Generated Summary:")
                st.write(response)
        else:
            st.warning("Please provide input text, PDF, or URL to summarize.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Aun Mohammad Kidwai")
