import datetime
import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import UpdateView, DetailView

from exam.forms import AddInternForm, CcEditInternForm
from exam.models import Exam


# @login_required
# def exam(request):
#     company = request.user.company
#     if company != "dm":
#         list_exam = Exam.objects.filter(cc=str(company))
#     else:
#         return render(request, 'exam/change_cc.html', {'title': 'Выбор КЦ', 'company': company})
#     context = {
#         'title': 'Зачеты',
#         'content': company,
#         'list_exam': list_exam,
#         'company': company,
#     }
#     # return render(request, 'exam/exam.html', context)
#     return render(request, 'exam/testing.html', context)
#
#
# @login_required
# def change_cc(request):
#     button_name = request.GET.get('btn')
#     list_exam = Exam.objects.filter(cc=str(button_name))
#     company = request.user.company
#     context = {
#         'title': button_name,
#         'content': button_name,
#         'list_exam': list_exam,
#         'company': company,
#     }
#     # return render(request, 'exam/exam.html', context)
#     return render(request, 'exam/testing.html', context)


# @login_required
# def exam_view(request):
#     # print(123)
#     # print(request.POST.get('exam_id', random.randint(100, 500)))
#     time = datetime.time(hour=0)
#     company = request.user.company
#     button_name = request.GET.get('btn', None)
#     form = AddInternForm()
#     if company == "dm" and not button_name:
#         return render(request, 'exam/change_cc.html', {'title': 'Выбор КЦ', 'company': company})
#
#     cc = button_name if company == "dm" else company
#     list_exam = Exam.objects.filter(cc=str(cc))
#     context = {
#         'title': button_name if button_name else 'Зачеты',
#         'content': cc,
#         'list_exam': list_exam,
#         'company': company,
#         'time': time,
#         'form': form,
#     }
#     return render(request, 'exam/testing.html', context)
#
#
# @login_required
# def add_intern(request):
#     if request.method == 'POST':
#         form = AddInternForm(request.POST)
#         if form.is_valid():
#             exam = form.save(commit=False)
#             exam.cc = request.user.company
#             form.save()
#             return redirect('exam:exam')
#
#     return render(request, 'exam/testing.html')
#
#
# @login_required
# def edit_intern(request, pk):
#     # print(123)
#     # print(request.POST.get('exam_id', random.randint(100, 500)))
#     exam = get_object_or_404(Exam, pk=pk)
#
#     if request.method == 'POST':
#         form = CcEditInternForm(request.POST, instance=exam)
#         # print(form)
#         # print(form.cleaned_data['name_intern'])
#         # print(form.cleaned_data['date_exam'])
#         if form.is_valid():
#             # Exam.object.filter(id=pk).update(
#             #     name_intern=form.cleaned_data['name_intern'],
#             #     date_exam=form.cleaned_data['date_exam'])
#             # exam.date_exam = form.cleaned_data['date_exam']
#             # exam.name_intern = form.cleaned_data['name_intern']
#             # exam.save(update_fields=('date_exam', 'name_intern'))
#             return redirect('exam:exam')
#     else:
#         form = CcEditInternForm(instance=exam)
#     return render(request, 'exam/testing.html', {'form': form})



# =====================================================================================================================

"""
Да, можно оптимизировать оба представления в одно, без потери качества. Объединение представлений может упростить код
и сделать его более поддерживаемым. Вот пример, как это можно сделать:

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from exam.models import Exam

@login_required
def exam_view(request):
    company = request.user.company
    button_name = request.GET.get('btn', None)
    
    if company == "dm" and not button_name:
        return render(request, 'exam/change_cc.html', {'title': 'Выбор КЦ', 'company': company})
    
    cc = button_name if company == "dm" else company
    list_exam = Exam.objects.filter(cc=str(cc))
    
    context = {
        'title': button_name if button_name else 'Зачеты',
        'content': cc,
        'list_exam': list_exam,
        'company': company,
    }
    
    return render(request, 'exam/testing.html', context)





Объяснение:

Импортируем необходимые модули и декораторы:

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from exam.models import Exam
Объединённое представление exam_view:

@login_required
def exam_view(request):
    company = request.user.company
    button_name = request.GET.get('btn', None)
    
    if company == "dm" and not button_name:
        return render(request, 'exam/change_cc.html', {'title': 'Выбор КЦ', 'company': company})
    
    cc = button_name if company == "dm" else company
    list_exam = Exam.objects.filter(cc=str(cc))
    
    context = {
        'title': button_name if button_name else 'Зачеты',
        'content': cc,
        'list_exam': list_exam,
        'company': company,
    }
    
    return render(request, 'exam/testing.html', context)
Как это работает:

Представление exam_view требует аутентификации пользователя.
Получаем компанию пользователя: company = request.user.company.
Получаем значение параметра btn из GET-запроса: button_name = request.GET.get('btn', None).
Если компания пользователя равна "dm" и параметр btn не передан, рендерим шаблон change_cc.html для выбора компании.
Определяем значение cc в зависимости от компании пользователя или параметра btn.
Фильтруем экзамены по значению cc и сохраняем их в list_exam.
Создаём контекст для шаблона и рендерим шаблон testing.html с этим контекстом.
Преимущества объединения:

Упрощение кода и уменьшение дублирования.
Лучшая поддерживаемость и читаемость кода.
Меньше вероятность ошибок при изменении логики представлений.
Таким образом, объединённое представление будет работать так же хорошо, как и два отдельных представления, и даже лучше с точки зрения поддерживаемости и читаемости кода.
"""
