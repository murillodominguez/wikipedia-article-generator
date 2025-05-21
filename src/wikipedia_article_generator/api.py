from fastapi import FastAPI
from pydantic import BaseModel
from crew import ArticleCrew

app = FastAPI()

class ArticleRequest(BaseModel):
    topic: str

@app.post("/generate_article/")
async def generate_article(request: ArticleRequest):
    research_agent = ArticleCrew.researcher()
    writer_agent = ArticleCrew.article_writer

    content = research_agent.(request)
    