from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, gsr namaste! how are you'

if __name__ == '__main__':
    app.run()

