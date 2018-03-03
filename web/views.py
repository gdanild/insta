from flask import redirect, render_template
from web import app
from web.forms import AddPostForm
from web.models import Post


@app.route('/', methods=['GET', 'POST'])
def main():
    form = AddPostForm(csrf_enabled=False)
    if form.validate_on_submit():

        data = [form.login.data,form.password.data]

        return redirect('/')
    return render_template('main.html', form=form)
