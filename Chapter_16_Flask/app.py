#todo update chapter 16 .. https://chatgpt.com/c/673df9f5-0c98-800f-b5b6-0dc1bde0239e .. update code to more explainable
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'  # Using SQLite as an example
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the database model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

@app.route('/')
def home():
    return "Welcome to the Blog"

@app.route('/post/<int:post_id>')
def show_post(post_id):
    with app.app_context():
        db.create_all()
        new_post = Post(title="My First Blog Post", content="This is the content of my first post!")
        db.session.add(new_post)
        db.session.commit()
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, content=post.content)



