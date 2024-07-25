import sys
import os
import pytest

# Добавляем путь к директории проекта в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

# Позитивный тест-кейс
def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode() == 'Hello, this is a response from Flask!'


# Негативный тест-кейс
def test_404_error(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404