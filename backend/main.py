from fastapi import FastAPI, UploadFile
from fastapi.middleware.cors import CORSMiddleware

from db import (
    init_db,
    get_counts,
    get_graph_edges,
    get_memory,
)

from rag import answer_from_knowledge
from research import run_research
from upload import process_txt_upload

app = FastAPI(title="EvolvIQ API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

init_db()

@app.get("/")
def home():
    return {"status": "running"}

@app.get("/counts")
def counts():
    return get_counts()

@app.post("/research")
def research(topic: str):
    return run_research(topic)

@app.post("/chat")
def chat(question: str):
    return answer_from_knowledge(question)

@app.get("/graph")
def graph():
    return get_graph_edges()

@app.get("/memory")
def memory():
    return get_memory()

@app.post("/upload")
async def upload(file: UploadFile):
    text = (await file.read()).decode("utf-8")
    return process_txt_upload(file.filename, text)
