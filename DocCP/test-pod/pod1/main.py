from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=["GET"])
def cpuup(r):
    n=2
    for i in range(100):
        #print(n)
        n=n*6

    return jsonify({'message': 'Pod1:Saccess!'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3100, debug=True)
