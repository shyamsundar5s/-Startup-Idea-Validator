import openai
from serpapi import GoogleSearch

class StartupIdeaValidator:
    def __init__(self):
        self.openai_api_key = "your-openai-api-key"
        self.serpapi_api_key = "your-serpapi-api-key"
        openai.api_key = self.openai_api_key

    def validate(self, idea: str) -> dict:
        competitors = self._find_competitors(idea)
        improvements = self._suggest_improvements(idea, competitors)
        market_demand = self._estimate_market_demand(idea)
        return {
            "idea": idea,
            "competitors": competitors,
            "improvements": improvements,
            "market_demand": market_demand
        }

    def _find_competitors(self, idea: str) -> list:
        query = f"competitors for {idea}"
        search = GoogleSearch({
            "q": query,
            "api_key": self.serpapi_api_key
        })
        results = search.get_dict()
        competitors = [result['title'] for result in results.get('organic_results', [])]
        return competitors

    def _suggest_improvements(self, idea: str, competitors: list) -> str:
        prompt = f"""
        The following business idea: "{idea}" has the following competitors: {competitors}.
        Suggest unique improvements or features to make this idea stand out.
        """
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=prompt,
            max_tokens=200
        )
        return response.choices[0].text.strip()

    def _estimate_market_demand(self, idea: str) -> str:
        # Replace this with a real data aggregation method for trend analysis
        demand_analysis_prompt = f"""
        Analyze the market demand for the following business idea: "{idea}".
        Consider current trends, customer needs, and potential growth.
        """
        response = openai.Completion.create(
            engine="gpt-4",
            prompt=demand_analysis_prompt,
            max_tokens=200
        )
        return response.choices[0].text.strip()
