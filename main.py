from fastapi import FastAPI
from src.models.summarize_text_request import SummarizeTextRequest

from src.openai_client import summarize_text

app = FastAPI()


@app.get("/about")
async def about():
    return {
        "about": "This api is for summarizing an input prompt and returning short summarized text. It is using ChatGPT for the summarization."
    }


@app.post("/summarize")
async def summarize(request: SummarizeTextRequest):
    response = summarize_text(request.text)
    return {"response": response}
