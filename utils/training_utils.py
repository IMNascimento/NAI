def tokenize_function(tokenizer):
    def tokenize(examples):
        return tokenizer(examples['text'], padding="max_length", truncation=True, max_length=128)
    return tokenize