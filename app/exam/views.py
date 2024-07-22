import datetime
import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator

from django.views.generic import UpdateView, DetailView, TemplateView, FormView

from exam.forms import AddInternForm
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


# @login_required
# def edit_intern(request, pk):
# print(123)
# print(request.POST.get('exam_id', random.randint(100, 500)))
# exam = get_object_or_404(Exam, pk=pk)

# if request.method == 'POST':
#     form = CcEditInternForm(request.POST, instance=exam)
# print(form)
# print(form.cleaned_data['name_intern'])
# print(form.cleaned_data['date_exam'])
# if form.is_valid():
# Exam.object.filter(id=pk).update(
#     name_intern=form.cleaned_data['name_intern'],
#     date_exam=form.cleaned_data['date_exam'])
# exam.date_exam = form.cleaned_data['date_exam']
# exam.name_intern = form.cleaned_data['name_intern']
# exam.save(update_fields=('date_exam', 'name_intern'))
# return redirect('exam:exam')
# else:
#     form = CcEditInternForm(instance=exam)
# return render(request, 'exam/testing.html', {'form': form})


# =====================================================================================================================


class ExamView(LoginRequiredMixin, TemplateView):
    template_name = 'exam/testing.html'

    def get(self, request, *args, **kwargs):
        company = request.user.company
        button_name = request.GET.get('btn', None)
        form = AddInternForm()

        if company == "dm" and not button_name:
            return render(request, 'exam/change_cc.html', {'title': 'Выбор КЦ', 'company': company})

        cc = button_name if company == "dm" else company
        list_exam = Exam.objects.filter(cc=str(cc))

        context = {
            'title': button_name if button_name else 'Зачеты',
            'content': cc,
            'list_exam': list_exam,
            'company': company,
            'time': datetime.time(hour=0),
            'form': form,
        }
        return self.render_to_response(context)


class AddInternView(LoginRequiredMixin, FormView):
    form_class = AddInternForm
    template_name = 'exam:exam'
    success_url = '/exam/'

    def form_valid(self, form):
        exam = form.save(commit=False)
        exam.cc = self.request.user.company
        print(exam.cc)
        exam.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


@method_decorator(login_required, name='dispatch')
class ExamUpdateView(UpdateView):
    model = Exam
    form_class = AddInternForm
    template_name = 'exam/update_intern.html'
    context_object_name = 'exam'

    def get_object(self, queryset=None):
        exam_id = self.kwargs.get('pk')
        return get_object_or_404(Exam, id=exam_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        exam = self.get_object()
        context['exam_date'] = exam.date_exam.strftime('%Y-%m-%d')
        context['list_exam'] = Exam.objects.filter(cc=self.request.user.company)
        return context

    def form_valid(self, form):
        exam = form.save(commit=False)
        exam.cc = self.request.user.company
        exam.save()
        return redirect('exam:exam')
