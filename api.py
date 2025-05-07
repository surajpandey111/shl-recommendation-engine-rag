from flask import Flask, request, jsonify, render_template_string
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

# Root route with a simple HTML form for testing
@app.route('/', methods=['GET'])
def home():
    html = """
    <h1>SHL Assessment Recommendation Engine</h1>
    <form method="POST" action="/recommend">
        <label for="query">Enter your query:</label><br>
        <input type="text" id="query" name="query" value="Which assessment for a manager in English with personality test?" style="width: 500px;"><br><br>
        <input type="submit" value="Get Recommendation">
    </form>
    <h2>Test GET Endpoint</h2>
    <p>You can also test the GET endpoint by visiting: <a href="/recommend-get?query=Which assessment for a manager in English with personality test?">Example GET Request</a></p>
    """
    return render_template_string(html)

# Existing POST endpoint
@app.route('/recommend', methods=['POST'])
def recommend():
    try:
        if request.form and 'query' in request.form:
            query = request.form['query']
        else:
            data = request.get_json()
            if not data or 'query' not in data:
                logger.warning("Invalid request: Missing query")
                return jsonify({"error": "Query is required in JSON body"}), 400
            query = data['query']

        if not query or not isinstance(query, str):
            logger.warning("Invalid query: Empty or not a string")
            return jsonify({"error": "Query must be a non-empty string"}), 400

        logger.info(f"Processing query: {query}")
        result = rag_engine.recommend(query)
        logger.info("Recommendation generated successfully")
        return jsonify(result)

    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

# New GET endpoint
@app.route('/recommend-get', methods=['GET'])
def recommend_get():
    try:
        query = request.args.get('query')
        if not query or not isinstance(query, str):
            logger.warning("Invalid query: Empty or not a string")
            return jsonify({"error": "Query must be a non-empty string in the query parameter"}), 400

        logger.info(f"Processing GET query: {query}")
        result = rag_engine.recommend(query)
        logger.info("Recommendation generated successfully")
        return jsonify(result)

    except Exception as e:
        logger.error(f"Error processing GET request: {str(e)}")
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)