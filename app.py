from flask import Flask,render_template,flash , redirect , url_for , session ,request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField , TextAreaField , PasswordField ,validators
from functools import wraps 


app=Flask(__name__)
app.debug = True
# print(Articles)

# data1 = cursor.execute('INSERT INTO users(name,email,username,password) VALUES("kim","1@naver.com","modu","1234")')

app.config['MYSQL_HOST']='127.0.0.1'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='1234'
app.config['MYSQL_DB']='myflaskapp'
app.config['MYSQL_CURSORCLASS']='DictCursor'

mysql = MySQL(app)

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

    #create cursor
    cur = mysql.connection.cursor()

    #get articles 
    result = cur.execute('SELECT * FROM articles')
    print(result)
    Articles = cur.fetchall()
    # print(Articles)
    
    if result>0:
        return render_template('articles.html', articles=Articles)
    
    else:
        return "아무 자료도 없어요!!!"

@app.route('/article/<string:id>')
def article(id):
    return render_template('article.html', id=int(id), articles=Articles)

class RegisterForm(Form):
    name=StringField('Name', [validators.Length(min=1,max=50)])
    username=StringField('Username', [validators.Length(min=4, max=25)])
    email=StringField('Email',[validators.Length(min=4, max=25)] )
    password=PasswordField('Password',[validators.DataRequired(), validators.EqualTo('confirm', message='passwords do not match')])
    confirm = PasswordField('Confirm password')

class ArticleForm(Form):
    title = StringField('Title', [validators.Length(min=1, max=50)])
    body = StringField('Body', [validators.Length(min=5, max=1000)])

@app.route('/register',methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name=form.name.data
        email=form.email.data
        username=form.username.data
        password=form.password.data

        cur = mysql.connection.cursor()

        cur.execute('INSERT INTO users(name,email,username,password) VALUES(%s,%s,%s,%s)', (name,email,username,password))

        mysql.connection.commit()

        cur.close()

        return "회원가입 완료 되었습니다."
    return render_template('register.html', form=form)

@app.route('/add_article', methods=['GET','POST'])
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title=form.title.data
        body=form.body.data

    # title="테스트"
    # author="park"
    # body="이것은 테스트2 입니다"

        cur = mysql.connection.cursor()

        cur.execute('INSERT INTO articles(title,body) VALUES(%s,%s)', (title,body))

        mysql.connection.commit()

        cur.close()

    return render_template('add_article.html' ,form=form)

if __name__ == '__main__':
    app.run(debug=True)
