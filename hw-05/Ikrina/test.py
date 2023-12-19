from fastapi.testclient import TestClient
from Ikrina_hw_05 import app

client = TestClient(app)


def test_read_hw_05():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "message": "Hi! If you see this message, API of light translator application works!>"}


def test_translate_hny():
    response = client.post("/translate", json={"text": "С новым годом!"})
    assert response.status_code == 200
    assert response.json() == {"translation_text": "Happy New Year!"}


def test_translate_christmas():
    response = client.post(
        "/translate", json={"text": "Все, что я хочу на Рождество, это ты!"})
    assert response.status_code == 200
    assert response.json() == {
        "translation_text": "All I want for Christmas is you!"}


def test_translate_name():
    response = client.post("/translate", json={"text": "Меня зовут Лена."})
    assert response.status_code == 200
    assert response.json() == {"translation_text": "My name is Lena."}
