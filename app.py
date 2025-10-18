from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the AWS DevOps Sample Microservice!",
        "status": "healthy"
    })

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    x = data.get('x', 0)
    y = data.get('y', 0)
    return jsonify({
        "x": x,
        "y": y,
        "sum": x + y
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
