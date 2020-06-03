from flask import Flask, jsonify, request
import github_requests
import os

app = Flask(__name__)

@app.route('/api/users')
def listusers():
	since = request.args.get("since")
	ret = github_requests.getUsers(since)
	return jsonify(ret)

@app.route('/api/users/<username>/details')
def userdetails(username):
	ret = github_requests.getUserDetails(username)
	return ret

@app.route('/api/users/<username>/repos')
def userrepos(username):
	ret = github_requests.getUserRepos(username)
	return jsonify(ret)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
