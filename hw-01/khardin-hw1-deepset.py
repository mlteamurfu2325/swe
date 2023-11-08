# https://huggingface.co/deepset/roberta-base-squad2

from transformers import pipeline


classifier = pipeline("question-answering", "deepset/roberta-base-squad2")

QA_input = {
    'question': 'What is a town?',
    'context': 
    "Taxi drivers in London are a special group. Driving a Taxi is a family tradition and many families have multiple generations behind the wheel. Before one can get a Taxi license one must drive around London for two years on a motorcycle learning the roads. So needless to say Taxi Drivers in London can get you anywhere you want to go and fast."
}

print(classifier(QA_input))

