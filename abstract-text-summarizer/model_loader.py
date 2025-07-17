# model_loader.py
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

def load_model():
    model_name = "ShivanshT247/abstractive-summarizer-model"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
    return tokenizer, model
