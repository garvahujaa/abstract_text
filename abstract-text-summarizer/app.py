import streamlit as st
from model_loader import load_model
from summerizer import generate_summary


@st.cache_resource
def get_model():
    return load_model()

tokenizer, model = get_model()

st.title("📝 Abstractive Text Summarizer")

text = st.text_area("Enter your text here", height=300)
min_len = st.slider("Minimum Length", 20, 100, 30)
max_len = st.slider("Maximum Length", 50, 300, 130)

if st.button("Summarize"):
    if not text.strip():
        st.warning("Please enter some input text.")
    else:
        with st.spinner("Summarizing..."):
            summary = generate_summary(text, tokenizer, model, min_len, max_len)
            st.text_area("Summary", summary, height=200)
