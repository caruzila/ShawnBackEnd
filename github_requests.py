import requests

apiUrl = 'https://api.github.com'
apiUrlUser = 'https://api.github.com/users/'

def getUsers(since):
    r = requests.get(apiUrl + '/users?since=' + since)
    ret = { "next": r.links["next"]["url"], "users": r.json()}
    return ret

def getUserDetails(name):
	r = requests.get(apiUrlUser + name)
	return r.json()

def getUserRepos(name):
	r = requests.get(apiUrlUser + name + '/repos')
	return r.json()
