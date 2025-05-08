# SHL Assessment Recommendation Engine (RAG Approach)

This repository contains the main implementation of the SHL Assessment Recommendation Engine for the SHL Research Intern application, using a Retrieval-Augmented Generation (RAG) approach. I have also included an alternative implementation using a more advanced RAG method with LangChain and FAISS, detailed below.

## Main Approach: SHL_Recommendation_RAG (Retrieval-Augmented Generation)

This project uses a RAG-based approach to recommend SHL assessments based on user queries. It includes a Streamlit web app for user interaction and a Flask API for generating recommendations.

- **Streamlit Web App**: [https://shl-recommendation-engine-rag-suraj.streamlit.app/](https://shl-recommendation-engine-rag-suraj.streamlit.app/)
- **Flask API**: [https://shl-recommendation-api-w7qe.onrender.com/recommend](https://shl-recommendation-api-w7qe.onrender.com/recommend) (Note: Hosted on Render’s free tier; first request may take 10–30 seconds due to cold starts.)
- **GitHub Repository (Streamlit App)**: [https://github.com/surajpandey111/shl-recommendation-engine-rag](https://github.com/surajpandey111/shl-recommendation-engine-rag)
- **GitHub Repository (Flask API)**: [https://github.com/surajpandey111/shl-recommendation-engine-rag-new](https://github.com/surajpandey111/shl-recommendation-engine-rag-new)

### Features
- **Retrieval**: Filters the SHL product catalog (`shl_product_catalog.csv`) based on query keywords (e.g., Job Level, Language, Test Type).
- **Generation**: Uses Google’s Gemini API to generate a concise recommendation.
- **User Interface**: A Streamlit web app where users can input queries and view recommendations and filtered assessments.
- **API**: A Flask API endpoint (`/recommend`) for programmatic access to recommendations.

## Alternative Approach: SHL_Recommendation (Advanced RAG with LangChain and FAISS)

This project uses a more advanced RAG implementation with LangChain, FAISS, and HuggingFace embeddings for semantic search, providing potentially more accurate retrieval for complex queries.

- **Streamlit Web App**: [https://shl-recommendation-engine-suraj.streamlit.app/](https://shl-recommendation-engine-suraj.streamlit.app/)
- **GitHub Repository**: [https://github.com/surajpandey111/shl-recommendation-engine](https://github.com/surajpandey111/shl-recommendation-engine)

### Features
- **Retrieval**: Uses LangChain and FAISS for vector-based semantic search with HuggingFace embeddings.
- **Generation**: Uses Google’s Gemini API for generating recommendations.
- **User Interface**: A Streamlit web app for inputting queries and viewing recommendations.

## Submission Details
This project was submitted as part of the SHL Research Intern application by Suraj Kumar Pandey. The main implementation (`SHL_Recommendation_RAG`) meets all requirements, including a web app and API endpoint. The alternative implementation (`SHL_Recommendation`) demonstrates an advanced RAG approach using modern NLP tools.
