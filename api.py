from flask import Flask, request, jsonify
from rag_engine import RAGEngine
import os
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the RAG engine
try:
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    if not gemini_api_key:
        raise ValueError("GEMINI_API_KEY environment variable not set")
    rag_engine = RAGEngine(gemini_api_key=gemini_api_key)
    logger.info("RAG Engine initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize RAG Engine: {str(e)}")
    raise

@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        # Get the query from the request
        data = request.get_json()
        if not data or 'query' not in data:
            logger.warning("Invalid request: Missing query")
            return jsonify({"error": "Query is required in JSON body"}), 400

        query = data['query']
        if not query or not isinstance(query, str):
            logger.warning("Invalid query: Empty or not a string")
            return jsonify({"error": "Query must be a non-empty string"}), 400

        logger.info(f"Processing query: {query}")
        # Get recommendation
        result = rag_engine.recommend(query)
        logger.info("Recommendation generated successfully")

        # Return JSON response
        return jsonify(result)

    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

if __name__ == "__main__":
    # Use the PORT environment variable if set (for Render), default to 5000 for local testing
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)