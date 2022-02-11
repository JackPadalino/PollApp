from django.http.response import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Question
from django.template import loader

# Create your views here.
def index(request):
    return HttpResponse('Hello! You are at the polls index!')

def details(request,question_id):
    question = get_object_or_404(Question,pk=question_id)
    return render(request,'polls/details.html',{'question':question})

def results(request,question_id):
    return HttpResponse(f"You are looking at the results of question {question_id}.")

def vote(request,question_id):
    return HttpResponse(f"You are voting on question {question_id}.")

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list':latest_question_list
    }
    #return HttpResponse(template.render(context,request))
    return render(request,'polls/index.html',context)
    