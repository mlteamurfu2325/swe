from transformers import pipeline

translator = pipeline("translation_ru_to_en", model="Helsinki-NLP/opus-mt-ru-en")

print(translator("Проживая в городе Москве, я могу учиться в магистратуре УрФУ дистационно ")[0]['translation_text'])

# Living in the city of Moscow, I can study at the Urfu Magistrate's School in a distancing manner.
