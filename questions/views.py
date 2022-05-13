from django.http import HttpResponse
from django.shortcuts import render
from .models import *


def index(request):
    rubrics = Rubric.objects.order_by('name')
    return render(request, 'questions/index.html', {'rubrics': rubrics})


def linc_by_rubric(request, rubric_id):
    #<a href="{% url 'linc_by_question' sub.pk %}">
    choosen_rubric = Rubric.objects.get(pk=rubric_id)
    choosen_rubric_subjects = Subjects.objects.filter(rubric=rubric_id)
    context = {'choosen_rubric': choosen_rubric, 'choosen_rubric_subjects': choosen_rubric_subjects, 'rubric_id': rubric_id}
    return render(request, 'questions/by_rubric.html', context)


def linc_by_question(request, rubric_id, question_id):
    #<a href="{{sub.pk}}">

    choosen_subject = Subjects.objects.get(pk=question_id)
    context = {'choosen_subject': choosen_subject}
    return render(request, 'questions/question_page.html', context)
