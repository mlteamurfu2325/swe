# ДЗ №1 по "Программной инженерии"
# https://huggingface.co/dslim/bert-base-NER

from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
from transformers import logging

logging.set_verbosity_error()

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "Microsoft opens a new campus in Florida in partnership with Google"

ner_results = nlp(example)
print(ner_results)

# [{'entity': 'B-ORG', 'score': 0.99847335, 'index': 1, 'word': 'Microsoft', 'start': 0, 'end': 9}, \
# {'entity': 'B-LOC', 'score': 0.9996697, 'index': 7, 'word': 'Florida', 'start': 32, 'end': 39}, \
# {'entity': 'B-ORG', 'score': 0.99826354, 'index': 11, 'word': 'Google', 'start': 60, 'end': 66}]
