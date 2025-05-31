from crewai import Agent
from wikipedia_search_tool import WikipediaSearchTool
from gemini_llm import create_gemini_llm

#class ResearcherAgent(Agent):
llm = create_gemini_llm()

class ResearcherAgent:
    def create(self):
        return Agent(
            role = "Pesquisador de Artigo Científico sobre {topic}",
            goal = "Pesquisa informação precisa e confiável sobre o tema {topic}",
            backstory = "Você é um pesquisador renomado que pesquisa artigos sobre o tema dado para você e compartilha suas conclusões com o agente escritor de artigos. Você se comunica apenas em Português Brasileiro.",
            verbose = True,
            llm = llm,
            allow_delegation=False
        )

class WriterAgent:
    def create(self):
        return Agent(
            role = "Escritor de Artigos sobre {topic}",
            goal = "Escreve um resumo sobre {topic} baseado na pesquisa feita pelo agente pesquisador.",
            backstory = "Você é um escritor renomado e criativo, capaz de resumir a informação da forma mais sucinta e didática sobre {topic}. Você escreve apenas em Português Brasileiro.",
            tools = [WikipediaSearchTool(base_url="http://pt.wikipedia.org/w/api.php")],
            verbose = True,
            llm = llm,
            allow_delegation = False
        )

