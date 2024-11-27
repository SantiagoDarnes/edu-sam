import pytest

def test_login(test_client):
    response = test_client.get("/login/")
    assert response.status_code == 200  # La pagina existe
    
    assert test_client.get("/home/student").status_code == 302  # Me redirecciona al login
    
    response = test_client.post("/login/", data={"username":"sdarnes", "password":"44011774"})
    assert response.status_code == 302  # Al ingresar, me redirecciona. Es un error en realidad
    response = test_client.get("/home/student")
    assert response.status_code == 200  # Si me deja ingresar a la pagina principal

