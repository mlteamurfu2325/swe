from fastapi.testclient import TestClient
from get_answer import app

client = TestClient(app)

def test_main_page():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Main page"}


def test_get_answer_1():
    response = client.post("/get_answer", json={"context": 
    """The Amazon rainforest (Portuguese: Floresta Amazônica or Amazônia; 
    Spanish: Selva Amazónica, Amazonía or usually Amazonia; French: Forêt amazonienne;
    Dutch: Amazoneregenwoud), also known in English as Amazonia or the Amazon Jungle, is
    a moist broadleaf forest that covers most of the Amazon basin of South America. This 
    basin encompasses 7,000,000 square kilometres (2,700,000 sq mi), of which 5,500,000 
    square kilometres (2,100,000 sq mi) are covered by the rainforest. This region includes
    territory belonging to nine nations. The majority of the forest is contained within 
    Brazil, with 60% of the rainforest, followed by Peru with 13%, Colombia with 10%, 
    and with minor amounts in Venezuela, Ecuador, Bolivia, Guyana, Suriname and French 
    Guiana. States or departments in four nations contain "Amazonas" in their names. T
    he Amazon represents over half of the planet's remaining rainforests, and comprises 
    the largest and most biodiverse tract of tropical rainforest in the world, with an 
    estimated 390 billion individual trees divided into 16,000 species.""", 
    
    "question": "Which name is also used to describe the Amazon rainforest in English?"})
    assert response.status_code == 200
    assert response.json() == "Amazonia or the Amazon Jungle"

def test_get_answer_2():
    response = client.post("/get_answer", json={"context": "My name is Wolfgang and I live in Berlin", 
    "question": "Where do I live?"})
    assert response.status_code == 200
    assert response.json() == "Berlin"

