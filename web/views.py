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
    if (not result['status'] == 'fail') and result['user']['is_private'] == False:
        res = [result["user"]["pk"],True]
        return res
    else:
        if result['status'] == 'fail':
            res = ["Unknown user",False]
            return res
        elif result['user']['is_private'] == True:
            res = ["It's a close profile",False]
            return res

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
                return render_template('main.html', form=form, error_login=True, mes = "Please check login or password")
            else:
                a = InList(api.getTotalSelfFollowers())  # Подписчики
                b = InList(api.getTotalSelfFollowings())  # подписки
                status_unfollow_funct = True
                # print("Подписчики: {}\nПодписки: {}".format(a,b))
        else:
            api = InstagramAPI("stolovka.1747", "ToYwjMHa698")
            api.login()
            user_id = GetPk(data[0],api)
            if user_id[1] == True:
                a = InList(api.getTotalFollowers(user_id[0]))
                b = InList(api.getTotalFollowings(user_id[0]))
            else:
                return render_template('main.html', form=form, error_login=True, mes = user_id[0])
            #print("Подписчики: {}\nПодписки: {}".format(len(a), len(b)))
            status_unfollow_funct = False

        return render_template('result.html', users=GenerateBadUsers(a, b),error_login = False, status = status_unfollow_funct)



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
