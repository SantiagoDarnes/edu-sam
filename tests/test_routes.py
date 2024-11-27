import pytest

def test_login(test_client):
    response = test_client.get("/login/")
    assert response.status_code == 200  # La pagina existe
    
    # Me redirecciona al login
    assert test_client.get("/home/student").status_code == 302
    
    # Test login
    response = test_client.post("/login/", data={"username":"sdarnes", "password":"44011774"})
    assert response.status_code == 302  # Al ingresar, me redirecciona. Es un error en realidad
    response = test_client.get("/home/student")
    assert response.status_code == 200  # Me deja ingresar a la pagina principal despues del login
    
    # Test registros de materias
    response = test_client.get("/subject_registration/")
    assert response.status_code == 200
    
    # Test registros de examenes
    response = test_client.get("/exam_registration/")
    assert response.status_code == 200
    
    # Test logout
    response = test_client.get("/login/logout")
    assert response.status_code == 302

    


