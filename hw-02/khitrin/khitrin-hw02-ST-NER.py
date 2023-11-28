import streamlit as st
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline


DEMO_TEXT = (
              "Google and YouTube are the two most visited"
              " websites worldwide followed by Facebook"
              " and X (formerly known as Twitter)."
            )


@st.cache_resource
def load_ner_model():
    tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
    model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
    return pipeline("ner", model=model, tokenizer=tokenizer)


st.title("Программная инженерия. ДЗ №2.")
st.markdown("### Извлечение сущностей (NER) из англоязычного текста.")
st.write("")

with st.form("ner_form"):
    raw_text = st.text_area(label="Введите текст:",
                            placeholder="Введите текст для извлечения сущностей, 10 000 знаков макс.",
                            value=DEMO_TEXT,
                            max_chars=10_000,
                            )
    submitted = st.form_submit_button("Извлечь")

st.write("")

if submitted:
    ner_extractor = load_ner_model()
    ner_results = ner_extractor(raw_text)

    if ner_results:
        marked_text = ""
        last_end = 0
        for res in ner_results:
            start = res["start"]
            end = res["end"]
            marked_text += raw_text[last_end:start]
            marked_text += f'<mark style="background-color: #D4F1F4;">{raw_text[start:end]}</mark>'
            last_end = end

        marked_text += raw_text[last_end:]

        st.subheader("Распознанные в тексте")

        st.markdown(marked_text, unsafe_allow_html=True)

        st.write("")

        entities = []
        for x in ner_results:
            entities.append((x["word"], x["entity"], x["start"], x["end"]))

        df = [{"Токен": token, "Тип сущности": entity,
               "Начальный индекс в строке": start,
               "Конечный индекс в строке": end}
              for token, entity, start, end in entities]

        st.subheader("Выделенные сущности")
        st.table(df)

    else:
        st.write("Именованные сущности не обнаружены.")
