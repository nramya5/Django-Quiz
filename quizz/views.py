from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import  login_required
from datetime import datetime

from .forms import  QuizForm

from .models import Quiz, Question, Answer

# Create your views here.

def index(request):
    '''sample check for redirections'''
    return HttpResponse('Hi')

@login_required
def quiz_list(request):
    ''' quiz listing'''
    q = Quiz.objects.all()
    print(q)
    return render(request, 'quizz_list.html', {'data': q})

@login_required
def quiz_new(request):
    ''' create a quiz form and submit'''
    formss = QuizForm(request.POST)
    return render(request, 'quiz_new.html', {'formss': formss})

@login_required
def quiz_form(request):
    ''' create a quiz form and submit and redirect to index'''
    context={}
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            form.save()
        context['form'] = form
    return redirect('index')

@login_required
def form_resp(request):
    #final_data= {}
    quiz_num= request.data['quiz_no']
    cnt= 0
    q= Quiz.objects.filter(quiz_name = quiz_num, user= request.user, created__lt = datetime.now())
    for que in  Question.objects.filter(quiz_no= quiz_num):
        for ans in Answer.objects.filter(quiz_no = quiz_num, question__in = que):
            if ans.is_correct:
                cnt+=1
    return render(request,'resp.html', {'cnt': cnt})


def qpage(request):
    questions = Quiz.objects.all()
    return render(request, 'quiz.html', {'questions': questions})
