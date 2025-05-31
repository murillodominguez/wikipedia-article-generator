from crewai import LLM
import os

def create_gemini_llm():
    llm = LLM(
        model="gemini/gemini-2.0-flash",
        api_key=os.getenv("GEMINI-API-KEY")
    )
    return llm