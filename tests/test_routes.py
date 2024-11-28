import pytest

def test_routes(test_client):
    response = test_client.get("/login/")
    assert response.status_code == 200  # La pagina existe
    
    # Test login
    response = test_client.post("/login/", data={"username":"sdarnes", "password":"44011774"})
    assert response.status_code == 302  # Al ingresar, me redirecciona
    test_client.get("/home/switch_profile/1")
    response = test_client.get("/home/student")
    assert response.status_code == 200  # Me deja ingresar a la pagina principal despues del login
    
    # Test registros de materias
    response = test_client.get("/subject_registration/")
    assert response.status_code == 200
    
    # Test registros de examenes
    response = test_client.get("/exam_registration/")
    assert response.status_code == 200
    
    # Test de reportes
    response = test_client.get("/reports/")
    assert response.status_code == 200
    
    # Test de trámites
    response = test_client.get("/procedures/")
    assert response.status_code == 200
    
    # Test de datos personales
    response = test_client.get("/personal_data/")
    assert response.status_code == 200
    
    # Test logout
    response = test_client.get("/login/logout")
    assert response.status_code == 302  # Me redirecciona de vuelta al login


def test_redirect(test_client):
    # Me redirecciona al login
    assert test_client.get("/home/student").status_code == 302
    
    # Test registros de materias
    response = test_client.get("/subject_registration/")
    assert response.status_code == 302
    
    # Test registros de examenes
    response = test_client.get("/exam_registration/")
    assert response.status_code == 302
    
    # Test de reportes
    response = test_client.get("/reports/")
    assert response.status_code == 302
    
    # Test de trámites
    response = test_client.get("/procedures/")
    assert response.status_code == 302
    
    # Test de datos personales
    response = test_client.get("/personal_data/")
    assert response.status_code == 302