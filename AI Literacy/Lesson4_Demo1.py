import os

import transformers
os.environ["USE_TF"] = "0"

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

print("Torch version:", torch.__version__)
print("Transformers version:", transformers.__version__)

text = "Generative AI helps small business move faster"


# Create a tokenizer and model for GPT-2
tok = AutoTokenizer.from_pretrained("gpt2")
# Tokenize the text, we can use the tokenizer's `tokenize` method, which splits the text into tokens, and the `encode` method, which converts the tokens into their corresponding IDs.
token = tok.tokenize(text)
#Encoding the text into IDs
ids = tok.encode(text)
#replace the special character "Ġ" with a space to make the tokens more readable
readable = [t.replace("Ġ", " ") for t in token]

print("Original text:", text)
print("Tokenized text:", token)
print("Encoded IDs:", ids)
print("Readable tokens:", readable)
print("Number of tokens:", len(token))