from crewai.tools import BaseTool
from pydantic import Field
import requests

class WikipediaSearchTool(BaseTool):
    base_url: str = Field("http://pt.wikipedia.org/w/api.php", description="URL base para requisição GET na API do wikipedia")
    name: str = "Wikipedia Search Tool"
    description: str = "Essa ferramenta busca informação da API do wikipedia."

    def _run(self, topic: str) -> str:
        params = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "exlimit": 1,
            "explaintext": 1,
            "titles": topic,
            "utf8": 1,
            "redirects": 1
        }
        response = requests.get(self.base_url, params=params)
        data = response.json()
        page = next(iter(data["query"]["pages"].values()))
        return page.get("extract", "Nenhuma Informação Encontrada")