import openai
from serpapi import GoogleSearch

class StartupIdeaValidator:
    def __init__(self):
        self.openai_api_key = "your-openai-api-key"
        self.serpapi_api_key = "your-serpapi-api-key"
        openai.api_key = self.openai_api_key

    def validate(self, idea: str, industry: str = None) -> dict:
        competitors = self._find_competitors(idea, industry)
        improvements = self._suggest_improvements(idea, competitors, industry)
        market_demand = self._estimate_market_demand(idea, industry)
        trends = self._get_trends(idea)  # Added trend visualization
        return {
            "idea": idea,
            "industry": industry,
            "competitors": competitors,
            "improvements": improvements,
            "market_demand": market_demand,
            "trends": trends
        }

    def _find_competitors(self, idea: str, industry: str = None) -> list:
        query = f"competitors for {idea}"
        if industry:
            query += f" in the {industry} industry"
        search = GoogleSearch({
            "q": query,
            "api_key": self.serpapi_api_key
        })
        results = search.get_dict()
        competitors = [result['title'] for result in results.get('organic_results', [])]
        return competitors

    def _suggest_improvements(self, idea: str, competitors: list, industry: str = None) -> str:
        prompt = f"""
        The following business idea: "{idea}" has the following competitors: {competitors}.
        Industry: {industry if industry else 'General'}.
        Suggest unique improvements or features to make this idea stand out.
        """
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=200
        )
        return response.choices[0].text.strip()

    def _estimate_market_demand(self, idea: str, industry: str = None) -> str:
        demand_analysis_prompt = f"""
        Analyze the market demand for the following business idea: "{idea}".
        Industry: {industry if industry else 'General'}.
        Consider current trends, customer needs, and potential growth.
        """
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=demand_analysis_prompt,
            max_tokens=200
        )
        return response.choices[0].text.strip()

    def _get_trends(self, idea: str) -> dict:
        # Placeholder for trend data; integrate with tools like Google Trends or custom APIs
        trends = {
            "dates": ["2025-01", "2025-02", "2025-03", "2025-04"],
            "values": [50, 65, 80, 90]  # Example data
        }
        return trends
