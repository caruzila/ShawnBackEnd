import json
import server
import pytest

apiUrl = 'https://api.github.com'
apiUrlUser = 'https://api.github.com/users/'

@pytest.fixture
def client():
	with server.app.test_client() as client:
		yield client

@pytest.fixture
def since():
	return "100"

@pytest.fixture
def name():
	return "caruzila"

def test_getUsers(client, since):
	rv = client.get(f'/api/users?since={since}')
	ret = json.loads(rv.data)
	assert rv.status_code == 200
	assert type(ret) is dict
	assert "next" in ret
	assert "users" in ret

def test_getUserDetails(client, name):
	rv = client.get(f'/api/users/{name}/details')
	ret = json.loads(rv.data)
	assert rv.status_code == 200
	assert type(ret) is dict

def test_getUserRepos(client, name):
	rv = client.get(f'/api/users/{name}/repos')
	ret = json.loads(rv.data)
	assert rv.status_code == 200
	assert type(ret) is list

