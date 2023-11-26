from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
	context: str
	question: str

app = FastAPI()
classifier = pipeline("question-answering", "deepset/roberta-base-squad2")


@app.get("/")
async def root():
	return {"message": "Main page"}


@app.post("/get_answer")
async def get_answer(item: Item):
	"Find answer for you question use context"
	QA_input = {"context": item.context, "question": item.question}
	data_json = classifier(QA_input)
	return data_json["answer"]
