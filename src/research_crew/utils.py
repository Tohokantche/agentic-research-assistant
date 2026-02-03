from crewai import LLM
import os 

def grok_llm(moel_name : str):
    return LLM(
    model = moel_name,
    base_url="https://api.groq.com/openai/v1",
    api_key = os.environ.get("GROQ_API_KEY"),  
)

def openai_llm():
    pass

def ollama_llm():
    pass