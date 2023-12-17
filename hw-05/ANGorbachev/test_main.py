from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "This is API of light translator application based on opus-mt-ru-en model from Helsinki-NL>"}


def test_translate_hello():
    response = client.post("/translate", json={"text": "Здравствуйте!"})
    assert response.status_code == 200
    assert response.json() == {"translation_text": "Hello!"}


def test_translate_santa():
    response = client.post("/translate", json={"text": "Я верю в Деда Мороза!"})
    assert response.status_code == 200
    assert response.json() == {"translation_text": "I believe in Santa Claus!"}

def test_translate_dont():
    response = client.post("/translate", json={"text": "Мне не нравится зима."})
    assert response.status_code == 200
    assert response.json() == {"translation_text": "I don't like winter."}
