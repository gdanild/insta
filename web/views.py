from flask import redirect, render_template
from web import app
from web.forms import AddPostForm
from .InstagramAPI import InstagramAPI

api = ""


def InList(a):
    res = []
    for i in a:
        res.append(i["username"])
    return res

def GetPk(username,api):
    api.searchUsername(username)
    result = api.LastJson
    if not result['status'] == 'fail':
        return result["user"]["pk"]
    else:
        raise Exception("Error username")

def GenerateBadUsers(a,b):
    res = []
    for i in b:
        if a.count(i) == 0:
            res.append(i)
    return res


@app.route('/', methods=['GET', 'POST'])
def main():
    form = AddPostForm(csrf_enabled=False)
    return render_template('main.html', form=form, error_login=False)


@app.route('/result', methods=['GET', 'POST'])
def result():
    global api
    form = AddPostForm(csrf_enabled=False)
    if form.validate_on_submit():
        data = [form.author.data, form.message.data]
        if len(data[1]) != 0:
            api = InstagramAPI(data[0], data[1])
            if (not api.login()):
                print("Can't login!")
                return render_template('main.html', form=form, error_login=True)
            else:
                a = InList(api.getTotalSelfFollowers())  # Подписчики
                b = InList(api.getTotalSelfFollowings())  # подписки
                status_unfollow_funct = True
                # print("Подписчики: {}\nПодписки: {}".format(a,b))
        else:
            api = InstagramAPI("stolovka.1747", "ToYwjMHa698")
            api.login()
            a = InList(api.getTotalFollowers(GetPk(data[0],api)))
            b = InList(api.getTotalFollowings(GetPk(data[0],api)))
            #print("Подписчики: {}\nПодписки: {}".format(len(a), len(b)))
            status_unfollow_funct = False

        return render_template('result.html', users=GenerateBadUsers(a, b), status = status_unfollow_funct)



    else:
        return redirect("/")


@app.route('/about_us', methods=['GET', 'POST'])
def about_us():
    return render_template('about_us.html')


@app.route('/unfollow/<id_user>', methods=['POST'])
def unfollow(id_user):
    global api
    api.searchUsername(id_user)
    a = api.LastJson['user']['pk']
    api.unfollow(a)
    print(api.LastJson)
    return
