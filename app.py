from flask import Flask, jsonify, request 
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__) 
auth = HTTPBasicAuth()

USER_DATA = {
    "admin": "Deep"
}

@auth.verify_password
def verify(username,password):
    if not (username and password):
        return False
    return USER_DATA.get(username) == password
 
Footballers = [{'name' : 'Lionel Messi'}, {'name' : 'Andres Iniesta'}, {'name' : 'Carlos Puyol'}, {'name' : 'Zinedine Zidane'}, {'name' : 'Xavi Hernandez'}, {'name' : 'Paolo Maldini'}, {'name' : 'Gianluigi Buffon'}, {'name' : 'Fabio Cannavaro'}, {'name' : 'Ronaldinho'}, {'name' : 'Ronaldo Nazario'}, {'name' : 'Andero Pirlo'}, {'name' : 'Francesco Totti'}, {'name' : 'Ricardo Kaka'}, {'name' : 'Sergio Ramos'}, {'name' : 'Oliver Kahn'}]

@app.route('/', methods=['GET'])
def test():
	return jsonify({'message' : 'The RESTful_api is working properly!'})

@app.route('/Player', methods=['GET'])
@auth.login_required
def returnAll():
	return jsonify({'Footballers' : Footballers})

@app.route('/Player/<string:name>', methods=['GET'])
@auth.login_required
def returnOne(name):
	Player = [Footballer for Footballer in Footballers if Footballer['name'] == name]
	return jsonify({'Footballer' : Players[0]})

@app.route('/Player', methods=['POST'])
@auth.login_required
def addOne():
	Footballer = {'name' : request.json['name']}

	Footballers.append(Footballer)
	return jsonify({'Footballers' : Footballers})

@app.route('/Player/<string:name>', methods=['PUT'])
@auth.login_required
def editOne(name):
	Players = [Footballer for Footballer in Footballers if Footballer['name'] == name]
	Players[0]['name'] = request.json['name']
	return jsonify({'Footballer' : Players[0]})

@app.route('/Player/<string:name>', methods=['DELETE'])
@auth.login_required
def removeOne(name):
	Player = [Footballer for Footballer in Footballers if Footballer['name'] == name]
	Footballers.remove(lang[0])
	return jsonify({'Footballers' : Footballers})

if __name__ == '__main__':
	app.run(debug=True)