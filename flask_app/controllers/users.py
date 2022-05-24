from flask_app import app
from flask import render_template, redirect, request, session,jsonify

from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html', users=users)

@app.route('/create/user', methods=['POST'])
def create_user():
    User.create_user(request.form)
    return jsonify(email=request.form['email'],user_name=request.form['user_name'])