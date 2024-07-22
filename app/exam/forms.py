from django import forms
from .models import Exam


class AddInternForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['date_exam', 'name_intern']

        widgets = {
            'date_exam': forms.DateInput(attrs={'type': 'date'})
        }


class EditInternForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['date_exam', 'name_intern', 'time_exam', 'name_examiner', 'result_exam', 'comment_exam']
