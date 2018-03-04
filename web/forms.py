from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField
from wtforms.validators import DataRequired, Length


class AddPostForm(FlaskForm):
    message = StringField("Пароль:  ")
    author =  StringField("Логин: ")
    submit = SubmitField("Отправить")
