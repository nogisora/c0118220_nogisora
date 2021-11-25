from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=["GET"])
def cpuup():
    n=2
    for i in range(100):
        print(n)
        n=n*4
    return jsonify({'message': 'Pod3:Saccess!'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
