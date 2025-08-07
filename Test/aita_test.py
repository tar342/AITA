
import sys
import os
import pytest

# Ensure Python can find app.py in the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app  # Flask app defined in app.py


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_post_empty_thread(client):
    """Test POST with empty thread returns error."""
    response = client.post('/', data={
        'thread': '',
        'user_role': 'Associate',
        'coworker_role': 'Manager',
        'relationship': 'peer'
    })
    assert response.status_code == 200
    assert b'Please enter an email thread' in response.data