from flask import Flask, render_template, request,redirect, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:$Tallone@Localhost/blog'
db = SQLAlchemy(app)

class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(50))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)

@app.route('/')
def index():
    posts = Blogpost.query.all()
    return render_template('index.html',posts = posts)

@app.route('/addpost', methods =['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    content = request.form['content']
    author = request.form['author']


    post = Blogpost(title=title,subtitle=subtitle,content=content,author=author,date_posted = datetime.now())
    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))

    return '<h1>Title : {} <br> Subtitle : {} <br > Author : {} <br> Content : {}</h1>'.format(title,subtitle, author, content)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()
    #date_posted = post.date_posted.strftime('%B %d, %Y')
    return render_template('post.html',post = post)
    """date_posted = date_posted"""

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug =True)