from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str

translator = pipeline("translation_ru_to_en", model="Helsinki-NLP/opus-mt-ru-en")

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "This is API of light translator application based on opus-mt-ru-en model from Helsinki-NL>


@app.post("/translate/")
async def translate(item: Item):
    return translator(item.text)[0]
