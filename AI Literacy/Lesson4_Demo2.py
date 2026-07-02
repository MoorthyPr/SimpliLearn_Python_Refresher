import os

import transformers
os.environ["USE_TF"] = "0"

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


text = "Generative AI helps small business move faster"


# Create a tokenizer and model for GPT-2
tok = AutoTokenizer.from_pretrained("gpt2")
# Tokenize the text, we can use the tokenizer's `tokenize` method, which splits the text into tokens, and the `encode` method, which converts the tokens into their corresponding IDs.
token = tok.tokenize(text)
#Encoding the text into IDs
ids = tok.encode(text)
#replace the special character "Ġ" with a space to make the tokens more readable
readable = [t.replace("Ġ", " ") for t in token]

model = AutoModelForCausalLM.from_pretrained("gpt2")
model.eval()

prompt = "The best way to grow a small business is to"

inpput_ids = tok.encode(prompt, return_tensors="pt")

with torch.no_grad():
    logits = model(inpput_ids).logits
    next_token_logits = logits[0, -1, :]
    probs = torch.softmax(next_token_logits, dim=-1)


top5 = torch.topk(probs, k=5)
print(f"Prompt: \"{prompt}\"\n")

print("Top 5 next token predictions:")
for score, idx in zip(top5.values, top5.indices):
    token = tok.decode(idx.item())
    print(f"Token: {token}, Score: {score.item():.4f}")
