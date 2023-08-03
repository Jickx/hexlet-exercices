from flask import Flask, request, render_template, jsonify, redirect
import json

app = Flask(__name__)


def get_users():
    with open('templates/users/db.txt', 'r') as f:
        users = json.load(f)
    return users


def append_new_user(user):
    with open('templates/users/db.txt', 'r') as f:
        data = json.load(f)
    data.append(user)
    with open('templates/users/db.txt', 'w') as f:
        json.dump(data, f)


def generate_id():
    with open('templates/users/db.txt', 'r') as f:
        data = json.loads(f.readlines()[-1])
    if data is None:
        return 1
    old_id = data['id']
    return old_id + 1


@app.route('/')
def index():
    return redirect('/users', 302)


@app.route('/users')
def show_users():
    users = get_users()
    return render_template(
        '/users/index.html',
        users=users
    )


@app.route('/users/new', )
def new_user():
    new_user = {
        'id': '',
        'nickname': '',
        'email': '',
    }
    return render_template(
        '/users/new.html',
        new_user=new_user
    )


@app.post('/users')
def add_new_user():
    new_user = request.form.to_dict()
    append_new_user(new_user)
    return redirect('/users', 302)
