from flask import Flask,render_template,flash , redirect , url_for , session ,request, logging
from flask_mysqldb import MySQL
from wtforms import Form, StringField , TextAreaField , PasswordField ,validators
from functools import wraps 
from passlib.hash import pbkdf2_sha256 # HASH 함수는 복호화 불가능

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
        password=pbkdf2_sha256.hash(str(form.password.data))

        cur = mysql.connection.cursor()

        cur.execute('INSERT INTO users(name,email,username,password) VALUES(%s,%s,%s,%s)', (name,email,username,password))

        mysql.connection.commit()

        cur.close()

        return "회원가입 완료 되었습니다."
    return render_template('register.html', form=form)

#GET 과 POST 둘다 해당 경로를 통해 적용하기 위함(조회와 생성을 하나로)
@app.route('/add_article', methods=['GET','POST'])
def add_article():
    form = ArticleForm(request.form)
    if request.method == 'POST' and form.validate():
        title=form.title.data
        body=form.body.data
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO articles(title,body) VALUES(%s,%s)', (title,body))
        mysql.connection.commit()
        cur.close()

    return render_template('add_article.html' ,form=form)
@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_cadidate = request.form['password']
        
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM users where username=%s",[username])
        if result > 0 :
            user = cur.fetchall()
            cur.close()
            password = user[0]['password']

            if pbkdf2_sha256.verify(password_cadidate, password):
                return redirect(url_for('articles'))
            else :
                return "비밀번호가 잘못되었어요"

        else :
            cur.close()
            return "존재하지 않는 ID입니다."

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
