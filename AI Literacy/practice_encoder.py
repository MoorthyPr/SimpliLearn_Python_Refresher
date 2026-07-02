import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


# Sample support examples for the encoder-only model
SUPPORT_EXAMPLES = pd.DataFrame(
    [
        {
            "text": "I was charged twice for my monthly subscription.",
            "category": "Billing",
        },
        {
            "text": "My payment failed but my card works everywhere else.",
            "category": "Billing",
        },
        {
            "text": "I need a copy of my invoice for last month.",
            "category": "Billing",
        },
        {
            "text": "I cannot log into my account after resetting my password.",
            "category": "Account Access",
        },
        {
            "text": "My two-factor authentication code is not working.",
            "category": "Account Access",
        },
        {
            "text": "I forgot my username and cannot access the dashboard.",
            "category": "Account Access",
        },
        {
            "text": "The dashboard loads slowly and sometimes freezes.",
            "category": "Technical Support",
        },
        {
            "text": "The app crashes whenever I upload a PDF file.",
            "category": "Technical Support",
        },
        {
            "text": "The report export button is not working.",
            "category": "Technical Support",
        },
        {
            "text": "How do I upgrade my plan to include more users?",
            "category": "Sales",
        },
        {
            "text": "Can someone explain your enterprise pricing?",
            "category": "Sales",
        },
        {
            "text": "I would like a demo for my team.",
            "category": "Sales",
        },
    ]
)


def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


model = load_model()

def encode_input_text(input_text):
    return model.encode(input_text,normalize_embeddings=True)


def encode_support_examples(support_examples):
    return encode_input_text(support_examples)


input_text = input("Enter your support request: ")
input_text_embedding = encode_input_text([input_text])
support_examples_embeddings = encode_support_examples(SUPPORT_EXAMPLES["text"].tolist())


# print("Input text embedding shape:", input_text_embedding)
# print("Support examples embeddings shape:", support_examples_embeddings)


similarities = cosine_similarity(input_text_embedding, support_examples_embeddings)[0]
print("Similarities ", similarities)

best_index = int(np.argmax(similarities))

predicted_category = SUPPORT_EXAMPLES.iloc[best_index]["category"]
confidence = float(similarities[best_index])

print(f"Best Index: {best_index}, Predicted Category: {predicted_category}, Confidence: {confidence:.4f}")

categoory_scores = (
    pd.DataFrame(
        {
            "category": SUPPORT_EXAMPLES["category"],
         "similarity": similarities
         }
         )
         .groupby("category", as_index=False)["similarity"]
         .max()
         .sort_values(by="similarity", ascending=False)
    )


print("Category Scores:\n", categoory_scores)