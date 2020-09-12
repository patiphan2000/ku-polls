from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You are at the polls index.")

def detail(request, question_id):
    return HttpResponse("You're look at question %s." %question_id)

def results(request, question_id):
    response = "Yore're look at the result of questoin %s."
    return HttpResponse(response %question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." %question_id)