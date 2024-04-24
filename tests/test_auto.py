import pytest
from datetime import datetime
from app import app, db
from app.models import User, Menu, Item

@pytest.fixture(scope='module')
def test_client():
    testing_client = app.test_client()

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    yield testing_client  # this is where the testing happens!

    ctx.pop()

def test_user_creation(test_client):
    # Create a user
    user = User(username='test_user', email='test@example.com')
    user.set_password('testpassword')

    # Add user to the database
    db.session.add(user)
    db.session.commit()

    # Retrieve the user from the database
    retrieved_user = User.query.filter_by(username='test_user').first()

    assert retrieved_user.username == 'test_user'
    assert retrieved_user.check_password('testpassword')

def test_menu_creation(test_client):
    # Create a menu
    menu = Menu(name='Test Menu')

    # Add menu to the database
    db.session.add(menu)
    db.session.commit()

    # Retrieve the menu from the database
    retrieved_menu = Menu.query.filter_by(name='Test Menu').first()

    assert retrieved_menu.name == 'Test Menu'
    assert isinstance(retrieved_menu.timestamp, datetime)

def test_item_creation(test_client):
    # Create an item
    item = Item(name='Test Item', supply=10, menu_id=1)

    # Add item to the database
    db.session.add(item)
    db.session.commit()

    # Retrieve the item from the database
    retrieved_item = Item.query.filter_by(name='Test Item').first()

    assert retrieved_item.name == 'Test Item'
    assert retrieved_item.supply == 10
    assert isinstance(retrieved_item.timestamp, datetime)

def test_item_removal(test_client):
    # Get item from the database
    item = Item.query.filter_by(name='Test Item').first()
    
    # Remove item from the database
    db.session.delete(item)
    db.session.commit()

    # Check if the item is still in the database
    retrieved_item = Item.query.filter_by(name='Test Item').first()
    assert retrieved_item.name != 'Test Item'
