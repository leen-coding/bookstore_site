from django.http import HttpResponse
# from django.template import loader
# t = loader.get_template("test_html.html")
# html = t.render()
# 方案一

# POST_FORM = '''
# <form method = "post" action = "/test_get_post">
#     name: <input type = "text" name ="username"><br \>
#     <input type ="submit" value ="125">
#     <img src ="/home/jialin/PycharmProjects/djangoProject/images.jpeg">
# </form>
# '''
from django.shortcuts import render


def say_hi():
    return "hi django@!"


class dog:
    def say(self):
        return "wangwang"


def view_get_post(request):
    if request.method == 'GET':
        # print(request.GET)
        # print(request.GET['a'])
        # print(request.GET.get('a',100))
        # print(request.GET.getlist('a'))
        dic = {}
        dic["str"] = "abcde"
        dic["int"] = 32
        dic["list"] = ["dfe", 626]
        dic["func"] = say_hi
        dic["dic"] = {"a": "2b"}
        dic["obj"] = dog()

        return render(request, 'test_html.html', dic)
    elif request.method == 'POST':
        print("username is " + request.POST["username"])
        return HttpResponse("post succuss")
    else:
        pass


def test_if_for(request):
    # dic = {"x": 3}
    dic = {"lst":[1,2,3,4]}
    return render(request, "test_if_for.html", dic)


def calculator(request):
    if request.method == "GET":
        return render(request, "cal.html")
    if request.method == "POST":
        x = int(request.POST['x'])
        y = int(request.POST['y'])
        op = request.POST['op']
        result = 0
        if op == 'add':
            result = x+y
        else:
            result =x-y
        return render(request, 'cal.html', locals())

def base(request):
    return render(request,'base.html')

def sport(request):
    return render(request,'sport.html')

def test_img(request):
    return render(request,'img_test.html')