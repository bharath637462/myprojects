from django import forms

from .models import Question, Choice


class Questionform(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = "__all__"
