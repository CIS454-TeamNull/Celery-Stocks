import pytest
from app import db 
from app.models import User

@pytest.fixture
def app():
    yield app

@pytest.fixture
def add_user(app):
    return app.test_adduser()

def test_adduser(adduser_fixture):
    assert adduser_fixture == True
    
