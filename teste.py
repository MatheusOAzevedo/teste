from flask import Flask

app = Flask(__name__)
@app.route('/inicio')
def ola():
    return '<h1> Teste </h1>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
