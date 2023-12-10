import streamlit as st
from transformers import pipeline


def create_model():
    model = pipeline("text-classification",
                     model="SkolkovoInstitute/russian_toxicity_classifier")
    return model


model = create_model()
st.title('Определение токсичности текста')
text = st.text_input('Введите текст', 'Конец 1980-х. Пока родители борются за выживание, брошенные всеми дети сбиваются в уличные стаи и бьются за асфальт. Буквально, чтобы контролировать всё, что стоит на «их» земле или передвигается по ней. Среди всеобщей нищеты — понятные правила жизни, поддержка и слово пацана, которое сильнее клятвы.')
result = st.button('Определить токсичность')

if result:
    res = model(text)
    sent = res[0]['label']
    if sent == 'toxic':
        st.write('Текст токсичный')
    else:
        st.write('Текст нейтральный')
