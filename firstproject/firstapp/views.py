import django.urls
from django.forms import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import FormView
from urllib import parse

from .forms import Questionform, ChoiceForm
from .models import Question, Choice


class IndexView(generic.ListView):
    template_name = 'firstapp/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.all()


class DetailView(generic.DetailView):
    model = Question
    template_name = 'firstapp/detail.html'
    form_class = ChoiceForm


def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request, 'firstapp/error.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(django.urls.reverse('firstapp:results', args=(question.id,)))


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'firstapp/results.html'


class ContactFormView(FormView):
    template_name = 'firstapp/detail.html'
    form_class = ChoiceForm
    success_url = '/'


class Createview(generic.CreateView):
    model = Question
    fields = ['question_text']
    template_name = 'firstapp/add.html'
    success_url = '/'

    # def get_success_url(self,  **kwargs):
        # return HttpResponseRedirect(django.urls.reverse('firstapp:results', args=(2)))
        # return reverse('firstapp:index', args=[self.slug])
        # HttpResponseRedirect(django.urls.reverse('index'))
        # return HttpResponseRedirect(self.request.GET.get('HTTP_ORIGIN', '/'))
        # return render(self.request, 'firstapp/index.html')
        # print(self.request.__dict__)
        # return self.request.GET.get('HTTP_ORIGIN')


class Choiceview(generic.CreateView):
    model = Question
    template_name = 'firstapp/choice.html'
    form_class = ChoiceForm
    success_url = '/'



class DeleteView(generic.DeleteView):
    model = Question
    template_name = 'firstapp/delete.html'
    success_url = '/'


class UpdateView(generic.UpdateView):
    model = Question
    template_name = 'firstapp/update.html'
    fields = [
        'question_text'
    ]
    success_url = "/"
