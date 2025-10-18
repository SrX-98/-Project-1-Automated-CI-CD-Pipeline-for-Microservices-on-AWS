import json
from app import app

def test_add():
    client = app.test_client()
    res = client.post('/add', json={'x': 2, 'y': 3})
    data = json.loads(res.data)
    assert data['sum'] == 5
