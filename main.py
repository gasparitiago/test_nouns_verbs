from fastapi import FastAPI
import json
import spacy

app = FastAPI()

@app.get("/{message}")
async def read_item(message):

    nlp = spacy.load("en_core_web_sm")
    doc = nlp(message)

    result = []
    for token in doc:
        result.append({token.text: token.pos_})

    return json(result)

@app.get("/")
async def root():
    return """Info: Write a phrase in the URL to get a response.
    """