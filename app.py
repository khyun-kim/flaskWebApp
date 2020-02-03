from flask import Flask

app = Flask(__name__)

app.debug = True

@app.route('/')
def hello():
    return '<h1>안녕하세요</h1>'

@app.route('/user/<name>')
def user(name):
    return '<h1>안녕하세요 %s!</h1>' %name

if __name__ == '__main__':
    app.run(debug=True)


