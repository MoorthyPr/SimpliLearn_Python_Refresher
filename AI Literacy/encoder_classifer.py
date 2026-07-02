# encoder_classifier_app.py
# AGS Course 02 - Lesson 02 (Transformers & NLP) - optional prototype for technical learners
#
# Prototype: Encoder-only business system (support ticket routing + semantic search).
# This is the ENCODER side of the lesson's "BERT understands, GPT generates" contrast.
# It turns text into embeddings and then classifies, ranks, and retrieves by meaning.
# It does NOT generate text. The companion RAG prototype (rag_assistant_app.py) adds
# the generation step.
#
# Run:
#   pip install streamlit sentence-transformers scikit-learn pandas numpy
#   streamlit run encoder_classifier_app.py

import numpy as np
import pandas as pd
import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


st.set_page_config(
    page_title="Encoder-Only Model Prototype",
    page_icon="🧠",
    layout="wide",
)


@st.cache_resource
def load_model():
    return SentenceTransformer("all-MiniLM-L6-v2")


model = load_model()


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


KNOWLEDGE_BASE = pd.DataFrame(
    [
        {
            "title": "Billing Refund Policy",
            "content": "Customers may request a refund within 14 days of billing if the service was not used extensively.",
        },
        {
            "title": "Password Reset Instructions",
            "content": "Users can reset their password from the login page by selecting Forgot Password and verifying their email.",
        },
        {
            "title": "Two-Factor Authentication Troubleshooting",
            "content": "If two-factor authentication fails, confirm device time sync, resend the code, or use backup codes.",
        },
        {
            "title": "PDF Upload Issues",
            "content": "PDF upload errors may occur when the file is encrypted, larger than 50MB, or contains unsupported embedded objects.",
        },
        {
            "title": "Enterprise Sales Demo",
            "content": "Enterprise customers can request a guided demo with pricing, security review, and implementation planning.",
        },
        {
            "title": "Report Export Troubleshooting",
            "content": "If report exports fail, check browser permissions, disable pop-up blockers, and retry with CSV format.",
        },
    ]
)


def embed_texts(texts):
    return model.encode(texts, normalize_embeddings=True)


@st.cache_data
def get_example_embeddings(texts):
    return embed_texts(texts)


def classify_ticket(ticket_text, examples_df):
    ticket_embedding = embed_texts([ticket_text])
    example_embeddings = get_example_embeddings(examples_df["text"].tolist())

    similarities = cosine_similarity(ticket_embedding, example_embeddings)[0]
    best_index = int(np.argmax(similarities))

    predicted_category = examples_df.iloc[best_index]["category"]
    confidence = float(similarities[best_index])

    category_scores = (
        pd.DataFrame(
            {
                "category": examples_df["category"],
                "similarity": similarities,
            }
        )
        .groupby("category", as_index=False)["similarity"]
        .max()
        .sort_values("similarity", ascending=False)
    )

    return predicted_category, confidence, category_scores


def semantic_search(query, kb_df, top_k=3):
    query_embedding = embed_texts([query])
    kb_embeddings = get_example_embeddings(kb_df["content"].tolist())

    similarities = cosine_similarity(query_embedding, kb_embeddings)[0]

    results = kb_df.copy()
    results["similarity"] = similarities

    return results.sort_values("similarity", ascending=False).head(top_k)


st.title("Encoder-Only Model Prototype")
st.caption("Business use case: support ticket routing + knowledge base retrieval")

st.markdown(
    """
This prototype uses an encoder model to convert text into embeddings.
It does **not generate text**. It classifies, ranks, and retrieves based on meaning.
"""
)

tab1, tab2, tab3 = st.tabs(
    [
        "Ticket Classifier",
        "Semantic Search",
        "Architecture",
    ]
)

with tab1:
    st.header("Support Ticket Classifier")

    ticket = st.text_area(
        "Enter a customer support ticket",
        value="I was charged twice and need help getting a refund.",
        height=120,
    )

    if st.button("Classify Ticket"):
        predicted_category, confidence, category_scores = classify_ticket(
            ticket,
            SUPPORT_EXAMPLES,
        )

        st.subheader("Prediction")
        st.metric("Predicted Category", predicted_category)
        st.metric("Similarity Score", f"{confidence:.3f}")

        st.subheader("Category Scores")
        st.dataframe(category_scores, use_container_width=True)

        st.info(
            "The encoder compared your ticket against labeled examples and selected the closest business category."
        )

    with st.expander("View training examples"):
        st.dataframe(SUPPORT_EXAMPLES, use_container_width=True)


with tab2:
    st.header("Semantic Knowledge Base Search")

    query = st.text_input(
        "Search the knowledge base",
        value="My PDF will not upload",
    )

    top_k = st.slider("Number of results", min_value=1, max_value=5, value=3)

    if st.button("Search Knowledge Base"):
        results = semantic_search(query, KNOWLEDGE_BASE, top_k=top_k)

        st.subheader("Retrieved Documents")

        for _, row in results.iterrows():
            st.markdown(f"### {row['title']}")
            st.write(row["content"])
            st.caption(f"Similarity score: {row['similarity']:.3f}")

        st.info(
            "The encoder converted the query and documents into vectors, then ranked documents by semantic similarity."
        )

    with st.expander("View knowledge base"):
        st.dataframe(KNOWLEDGE_BASE, use_container_width=True)


with tab3:
    st.header("Prototype Architecture")

    st.code(
        """
Customer Ticket / Search Query
        ↓
Encoder-Only Model
        ↓
Text Embedding
        ↓
Similarity Search or Classification
        ↓
Business Output
        ↓
Human Review / Workflow Automation
        """,
        language="text",
    )

    st.markdown(
        """
### What this prototype demonstrates

- Text classification
- Semantic search
- Embedding-based similarity
- Encoder-only model behavior
- Human-in-the-loop business workflow

### What production would add

- API endpoint with FastAPI
- Database for tickets and labels
- Vector database such as pgvector, Qdrant, Pinecone, or FAISS
- Authentication and access control
- Monitoring for accuracy, drift, latency, and human overrides
- Feedback loop for retraining
"""
    )
