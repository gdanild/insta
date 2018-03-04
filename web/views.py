from flask import redirect, render_template
from web import app
from web.forms import AddPostForm
from web.models import Post
from .InstagramAPI import InstagramAPI

def InList(a):
    res = []
    for i in a:
        res.append(i["username"])
    return res

@app.route('/', methods=['GET', 'POST'])
def main():
    form = AddPostForm(csrf_enabled=False)
    if form.validate_on_submit():
        data = [form.author.data,form.message.data]
        api = InstagramAPI(data[0], data[1])
        if (api.login()):
            a = InList(api.getTotalSelfFollowers()) #Подписчики
            b = InList(api.getTotalSelfFollowings()) #подписки
            res = []
            for i in b:
                if a.count(i) == 0:
                    res.append(i)
            print (res)
            #print("Подписчики: {}\nПодписки: {}".format(a,b))
            print("Login succes!")
            return render_template('main.html', form=form, lol=3,users=res)
        else:
            print("Can't login!")
            return render_template('main.html', form=form, lol=0)
    return render_template('main.html', form=form, lol=1)
