from database_package.db_session import global_init, create_session
from database_package.Users import User

from flask_login import LoginManager, current_user, logout_user, login_required, login_user
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm

from models import LoginForm, RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mega_secret_key'
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    session = create_session()
    return session.query(User).get(user_id)


def main():
    global_init("db.db")
    app.run()


@app.route('/')
def index():
    return render_template("main.html", title="main")

@app.route("/login", methods=["POST", "GET"])
def login():
    form: FlaskForm = LoginForm()
    if form.validate_on_submit():
        return redirect("/")
    return render_template("login.html", title="login", form=form)

if __name__ == '__main__':
    main()
