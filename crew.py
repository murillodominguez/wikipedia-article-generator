from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from agents import ResearcherAgent, WriterAgent
from typing import List

@CrewBase
class ArticleCrew():

    def __init__(self):
        self.researcher = ResearcherAgent().create()
        self.writer = WriterAgent().create()

    tasks: List[Task]

    @task
    def research_task(self) -> Task:
        return Task(    
            description = "Conduzir uma pesquisa criteriosa e extensa sobre {topic}",
            expected_output = "Um texto para o escritor interpretar e escrever um resumo",
            agent = self.researcher
        )

    @task
    def writing_task(self) -> Task:
        return Task(
            description = "Analisar o texto feito pelo pesquisador e baseado nisso, escrever o artigo mais refletido e confiável sobre {topic}",
            expected_output = "Um artigo completo sobre o tópico {topic}, com no mínimo {words} palavras",
            agent = self.writer
        )

    @crew
    def crew(self) -> Crew:

        return Crew(
            agents= [self.researcher, self.writer],
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
