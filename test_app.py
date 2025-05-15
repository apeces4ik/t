import pytest
from app import app

  @pytest.fixture
  def client():
      app.config['TESTING'] = True
      with app.test_client() as client:
          yield client

  def test_time_endpoint(client):
      response = client.get('/time')
      data = response.get_json()
      assert response.status_code == 200
      assert 'time' in data
      assert data['time'] != 0
