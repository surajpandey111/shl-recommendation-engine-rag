import streamlit as st
from rag_engine import RAGEngine
import os

# Initialize the RAG engine
rag_engine = RAGEngine(gemini_api_key=os.getenv("GEMINI_API_KEY"))

# Streamlit app
st.title("SHL Assessment Recommendation Engine")
st.write("Enter a query to get a recommended SHL assessment.")

# Input query
query = st.text_input("Your Query:", "Which assessment for a manager in English with personality test?")

if st.button("Get Recommendation"):
    if query:
        # Get recommendation
        result = rag_engine.recommend(query)
        
        # Display results
        st.subheader("Recommendation")
        st.write(result["recommendation"])
        
        st.subheader("Filtered Assessments")
        for assessment in result["filtered_assessments"]:
            st.write(f"**Product Name**: {assessment['Product Name']}")
            st.write(f"**Description**: {assessment['Description']}")
            st.write(f"**Job Level**: {assessment['Job Level']}")
            st.write(f"**Languages**: {assessment['Languages']}")
            st.write(f"**Test Type**: {assessment['Test Type']}")
            st.write("---")
    else:
        st.error("Please enter a query.")