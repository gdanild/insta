from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length


class AddPostForm(FlaskForm):
    message = PasswordField("Пароль:  ")
    author =  StringField("Логин: ")
    submit = SubmitField("Отправить")
