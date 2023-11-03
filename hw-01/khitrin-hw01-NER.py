# ДЗ №1 по "Программное инженерии"
# https://huggingface.co/dslim/bert-base-NER

from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = "Microsoft opens a new campus in Florida in partnership with Google"

ner_results = nlp(example)
print(ner_results)
