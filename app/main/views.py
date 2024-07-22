from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from users.models import User


@login_required
def index(request):
    company = request.user.company
    # list_person = User.objects.filter(company__startswith='cc')
    list_person = User.objects.all()
    context = {
        'title': 'Главная',
        'content': 'Главная страница',
        'company': company,
        'id': company,
        'list_person': list_person,
    }
    return render(request, 'main/index.html', context)


@login_required
def index_main(request):
    company = request.user.company
    # list_person = User.objects.filter(company__startswith='cc')
    list_person = User.objects.all()
    context = {
        'title': 'Главная',
        'content': 'Главная страница',
        'company': company,
        'list_person': list_person,
    }
    return render(request, 'main/index_main.html', context)


@login_required
def about(request):
    company = request.user.company
    context = {
        'title': 'About',
        'content': 'About-Page',
        'company': company,
    }
    return render(request, 'main/about.html', context)


@login_required
def dm(request):
    context = {
        'title': 'DM',
        'content': 'DM',
    }
    return render(request, 'main/dm.html', context)


@login_required
def cc_1(request):
    context = {
        'title': 'CC_1',
        'content': 'CC_1',
    }
    return render(request, 'main/cc_1.html', context)


@login_required
def cc_2(request):
    context = {
        'title': 'CC_2',
        'content': 'CC_2',
    }
    return render(request, 'main/cc_2.html', context)
