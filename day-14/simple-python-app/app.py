from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, bagunnara ledu bagunnara skljdfhiusdhfkjhsdfhsdi'

if __name__ == '__main__':
    app.run()

