from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.contrib.auth import logout
from django.http import HttpResponse

'''用户注册的方法'''


def sign_up(request):
    state = None
    if request.method == 'POST':

        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repeat_password', '')
        # email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        if User.objects.filter(username=username):
            state = 'user_exist'

            return HttpResponse(state)
        else:
            # new_user = User.objects.create_user(username=username, password=password, email=email)
            new_user = User.objects.create_user(username=username, password=password, )
            # new_user.save()

            print("****************************")
            print(new_user)

            return HttpResponse(new_user)
