from wtforms import EmailField, StringField, SubmitField, PasswordField
from wtforms.validators import Email, DataRequired
from flask_wtf import FlaskForm

class RegisterForm(FlaskForm):
    name = StringField("Имя", validators=[DataRequired()])
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль")
    submit = SubmitField("Регистрация")

class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Пароль")
    submit = SubmitField("Регистрация")