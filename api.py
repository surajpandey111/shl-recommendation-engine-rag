from flask import Flask, request, jsonify
from rag_engine import RAGEngine
import os

app = Flask(__name__)

# Initialize the RAG engine
rag_engine = RAGEngine(gemini_api_key=os.getenv("GEMINI_API_KEY"))

@app.route('/recommend', methods=['POST'])
def recommend():
    # Get the query from the request
    data = request.get_json()
    query = data.get('query', '')

    if not query:
        return jsonify({"error": "Query is required"}), 400

    # Get recommendation
    result = rag_engine.recommend(query)

    # Return JSON response
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)