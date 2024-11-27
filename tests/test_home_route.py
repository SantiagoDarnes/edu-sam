
# import pytest

# def test_home():
#     app_ = create_app()
#     assert type(app_.url_map) == dict
#     with app_.test_client() as client:
#         response = client.post("/login", data=dict(username="sdarnes", password="44011774"))
#         response2 = client.get("/home/student")
#         assert response.status_code == 200
#         assert response2.status_code == 200

def test_login(test_client):
    response = test_client.get("/login/")
    assert response.status_code == 200
    
    response = test_client.post("/login/", data={"username":"sdarnes", "password":"44011774"})
    assert response.status_code == 200