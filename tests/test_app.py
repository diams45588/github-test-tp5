import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Bienvenue' in response.data

def test_hello_route(client):
    response = client.get('/hello/Alice')
    assert response.status_code == 200
    assert b'Alice' in response.data

def test_add_route(client):
    response = client.get('/add/5/3')
    assert response.status_code == 200
    assert b'8' in response.data

def test_api_data_route(client):
    response = client.get('/api/data')
    assert response.status_code == 200
    assert b'data' in response.data

def test_404_route(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404
