# src/tests/test_ping.py


import json


def test_ping(test_app):
    # Given
    client = test_app.test_client()

    # When
    resp = client.get('/ping')
    data = json.loads(resp.data.decode())

    # Then
    assert resp.status_code == 200
    assert 'pong is alive in 2021 !' in data['message']
    assert 'success' in data['status']