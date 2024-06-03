from transformers import GPT2LMHeadModel, GPT2Tokenizer
from config.config import Config

tokenizer = GPT2Tokenizer.from_pretrained(Config.MODEL_PATH)
model = GPT2LMHeadModel.from_pretrained(Config.MODEL_PATH)

def generate_text(input_text):
    input_ids = tokenizer.encode(input_text, return_tensors='pt')
    output = model.generate(input_ids, max_length=100, num_return_sequences=1)
    return tokenizer.decode(output[0], skip_special_tokens=True)