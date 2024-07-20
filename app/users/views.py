from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse

from users.forms import UserloginForm
from users.models import User


# def login(request: HttpResponse):
#     if request.method == 'POST':
#         form = UserloginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = authenticate(request, username=username, password=password)
#
#             # a = User.objects.filter(username=user)
#             # print(a[0].company)
#             user_name = user.username
#             company = user.company
#             post = user.post
#
#             print(f"username - {user_name}\ncompany - {company}\npost - {post}")
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('main:index'))
#     else:
#         form = UserloginForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'users/login.html', context)


def login_view(request: HttpRequest):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect("/")

        # return render(request, 'users/login.html')
        return render(request, 'users/auth.html')

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    # user_name = user.username
    # company = user.company
    # post = user.post
    # print(f"username - {user_name}\ncompany - {company}\npost - {post}")
    if user is not None:
        login(request, user)
        return redirect("/")

    # return render(request, 'users/login.html', {"error": "Invalid login"})
    return render(request, 'users/auth.html', {"error": "Invalid login"})
