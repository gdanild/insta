from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired, Length


class AddPostForm(FlaskForm):
    message = StringField("Логин:  ")
    author =  StringField("Пароль: ")
    submit = SubmitField("Отправить")
