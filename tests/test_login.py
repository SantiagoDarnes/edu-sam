
def test_login_student(test_client):
    response = test_client.get("/home/student")
    assert response.status_code == 302  # Me redirecciona al login
    
    test_client.post("/login/", data={"username":"sdarnes", "password":"44011774"})
    response = test_client.get("/home/student")
    assert response.status_code == 200  # Ahora si me deja entrar a /home/student
    
    response = test_client.get("/login/logout")
    assert response.status_code == 302  # Cerré la sesion asi que me redirecciona al login
    
    response = test_client.get("/home/student")
    assert response.status_code == 302  # Efectivamente no me deja volver a /home


def test_login_admin(test_client):
    response = test_client.get("/home/admin")
    assert response.status_code == 302  # Me redirecciona al login
    
    test_client.post("/login/", data={"username":"sdarnes", "password":"44011774"})
    response = test_client.get("/home/switch_profile/3")
    assert response.status_code == 302
    response = test_client.get("/home/admin")
    assert response.status_code == 200  # Ahora si me deja entrar a /home/admin
    
    response = test_client.get("/login/logout")
    assert response.status_code == 302  # Cerré la sesion asi que me redirecciona al login
    
    response = test_client.get("/home/admin")
    assert response.status_code == 302  # Efectivamente no me deja volver a /home