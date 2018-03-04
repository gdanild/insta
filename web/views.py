from flask import redirect, render_template
from web import app
from web.forms import AddPostForm
from web.models import Post
from .InstagramAPI import InstagramAPI

def InList(a):
    b = a["users"]
    res = []
    for i in b:
        res.append(i["username"])
    return res

@app.route('/', methods=['GET', 'POST'])
def main():
    form = AddPostForm(csrf_enabled=False)
    if form.validate_on_submit():

        data = [form.author.data,form.message.data]
        api = InstagramAPI(data[0], data[1])
        if (api.login()):
            api.getSelfUserFollowers()  # подписчики
            folow_to_me = InList(api.LastJson)# print last response JSON
            api.getSelfUsersFollowing() # подписки
            i_folow = InList(api.LastJson)
            print ("Подписки: " + str(len(i_folow)))
            print ("Подписчки: " + str(len(folow_to_me)))
            print("Login succes!")
        else:
            print("Can't login!")
            return render_template('main.html', form=form, lol=0)
    return render_template('main.html', form=form, lol=1)
