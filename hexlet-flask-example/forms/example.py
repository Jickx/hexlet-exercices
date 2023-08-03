from flask import Flask, render_template
from flask import request

app = Flask(__name__)


users = ['mike', 'mishel', 'adel', 'keks', 'kamila']


@app.route('/users')
def search():
    term = request.args.get('term')
    filtered_users = filter(lambda user: str(term) in user, users)
    if term is None:
        term = ''
    return render_template(
        'users/index.html',
        users=list(filtered_users),
        search=term,
    )
