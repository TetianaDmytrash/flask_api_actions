from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, this is a response from Flask!', 200

if __name__ == '__main__':
    app.run(debug=True)
