import flask
import flask_login

app = flask.Flask(__name__)


@app.route('/')
@app.route('/login')
def login():
    return flask.render_template('login.html', title='Please sign in')