import pandas as pd
import google.generativeai as genai

class RAGEngine:
    def __init__(self, gemini_api_key, csv_path="shl_product_catalog.csv"):
        # Configure Gemini API
        genai.configure(api_key=gemini_api_key)
        self.model = genai.GenerativeModel('gemini-2.0-flash')  # Update this if your model name is different
        # Load the product catalog
        self.df = pd.read_csv(csv_path)
        # Fill NaN values to avoid issues with str.contains
        self.df["Job Level"] = self.df["Job Level"].fillna("")
        self.df["Languages"] = self.df["Languages"].fillna("")
        self.df["Test Type"] = self.df["Test Type"].fillna("")

    def retrieve(self, query):
        # Extract Job Level from the query
        job_levels = ["Director", "Entry-Level", "Executive", "General Population", 
                      "Graduate", "Manager", "Mid-Professional", "Front Line Manager", "Supervisor"]
        matched_job_level = next((jl for jl in job_levels if jl.lower() in query.lower()), None)

        # Extract Language from the query
        languages = ["English", "Spanish", "French", "German", "Portuguese", "Chinese", "Japanese"]
        matched_language = next((lang for lang in languages if lang.lower() in query.lower()), None)

        # Extract Test Type from the query
        test_types = ["Personality", "Behavior", "Simulation", "Ability", "Aptitude", "Biodata", "Situational Judgement"]
        matched_test_type = next((tt for tt in test_types if tt.lower() in query.lower()), None)

        # Filter the catalog
        filtered_df = self.df
        if matched_job_level:
            filtered_df = filtered_df[filtered_df["Job Level"].str.contains(matched_job_level, case=False, na=False)]
        if matched_language:
            filtered_df = filtered_df[filtered_df["Languages"].str.contains(matched_language, case=False, na=False)]
        if matched_test_type:
            filtered_df = filtered_df[filtered_df["Test Type"].str.contains(matched_test_type, case=False, na=False)]

        # If no filters matched, return the top 5 rows as a fallback
        if filtered_df.empty:
            filtered_df = self.df.head(5)

        return filtered_df

    def generate(self, query, retrieved_df):
        # Convert retrieved data to string for Gemini
        catalog_str = retrieved_df.to_string(index=False)
        # Generate recommendation using Gemini
        prompt = f"Based on the following SHL assessment catalog, recommend an assessment for this query: '{query}'\n\n{catalog_str}\n\nProvide a concise recommendation (1-2 sentences)."
        try:
            response = self.model.generate_content(prompt)
            recommendation = response.text
        except Exception as e:
            recommendation = f"Error generating recommendation: {str(e)}"
        return recommendation

    def recommend(self, query):
        # Step 1: Retrieve relevant assessments
        retrieved_df = self.retrieve(query)
        # Step 2: Generate a recommendation
        recommendation = self.generate(query, retrieved_df)
        # Step 3: Return the result
        return {
            "query": query,
            "recommendation": recommendation,
            "filtered_assessments": retrieved_df.to_dict(orient="records")
        }
        