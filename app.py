from flask import Flask,render_template
from data import Articles
from flask_mysqldb import MySQL
import pymysql

app=Flask(__name__)
app.debug = True
Articles = Articles()
print(Articles)

db = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='1234', db='myflaskapp', charset='utf8')

cursor = db.cursor()

data1 = cursor.execute('INSERT INTO users(name,email,username,password) VALUES("kim","1@naver.com","modu","1234")')
print(data1)
# app.config['MYSQL_HOST']='127.0.0.1'
# app.config['MYSQL_USER']='root'
# app.config['MYSQL_PASSWORD']='1234'
# app.config['MYSQL_DB']='myflaskapp'
# app.config['MYSQL_CURSORCLASS']='DictCursor'

# MySQL(app).connection.cursor()
@app.route('/')
def hello():
    return render_template('home.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles)

@app.route('/article/<string:id>')
def article(id):
    return render_template('article.html', id=int(id), articles=Articles)

if __name__ == '__main__':
    app.run(debug=True)
