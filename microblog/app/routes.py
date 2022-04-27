from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Anas'}
    posts = [
        {
            'author': {'username': 'Fauzi'},
            'body': 'Beautiful day in Kudus!'
        },
        {
            'author': {'username': 'Tom'},
            'body': 'Beautiful day in Bali!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)