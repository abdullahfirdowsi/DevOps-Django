from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template import loader

def todo(request):
    template=loader.get_template('todo.html')
    return HttpResponse(template.render({},request))

def calculator(request):
    template = loader.get_template('calculator.html')
    return HttpResponse(template.render({},request))
