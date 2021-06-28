from django.http.response import HttpResponsePermanentRedirect
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hellow world you're at the polls index")

# Create your views here.
def detail(request, question_id):
    response = "You're looking at the results of questions"
    return HttpResponse (response)