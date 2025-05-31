from fastapi import FastAPI
from crew import ArticleCrew
from article import Article
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/generate-article/", response_model = Article)
def generate_article(topic: str, words: str):
    crew = ArticleCrew().crew()
    result = crew.kickoff(inputs={"topic": topic, "words": words})

    content = str(result)
    keywords = topic.split()

    article = Article(
        title = topic,
        content = content,
        keywords = keywords
    )

    return article

@app.get("/",response_class = HTMLResponse)
def home():
    return open("index.html", encoding="utf-8").read()