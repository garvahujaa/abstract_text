def generate_summary(text, tokenizer, model, min_length=30, max_length=130):
    if not text.strip():
        return "⚠️ Input text is empty."

    inputs = tokenizer.encode(text, return_tensors="pt", truncation=True, max_length=1024)
    summary_ids = model.generate(
        inputs,
        min_length=min_length,
        max_length=max_length,
        length_penalty=2.0,
        num_beams=4,
        early_stopping=True
    )
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)
