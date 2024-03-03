from transformers import pipeline
import streamlit as st
import time


@st.cache_resource
def load_model():
	return pipeline("question-answering", "deepset/roberta-base-squad2")


def load_context():
	return st.text_area("Context", placeholder="Please input context for you question")


def load_question():
	return st.text_input("Answer", placeholder="Please input you question")


def print_answer(answer):
	st.write("*Answer*: " + answer["answer"])


def load_info():
        st.title('Question&Answer')
        st.subheader('Find answer for you question in context')

def progress_info():
	my_bar = st.progress(0, text="Find answer. Please wait.")

	for percent_complete in range(100):
		my_bar.progress(percent_complete + 1, text="Find answer. Please wait.")
		time.sleep(0.05)
	my_bar.empty()
	st.success("Done! ",  icon="✅")



if __name__ == "__main__":
	load_info()
	classifier = load_model()
	QA_input = {"context": load_context(), "question": load_question()}
	click = st.button('Get answer')

	if click:
		progress_info()
		print_answer(classifier(QA_input))

# update7 for test flake8 
