from flask import render_template, Blueprint
users=Blueprint('users', __name__)

@users.route('/users')
def users_home():
    return render_template('users.html', title='users')

@users.route('/register')
def register():
    return render_template('register.html')

@users.route('/login')
def login():
    return render_template('login.html')