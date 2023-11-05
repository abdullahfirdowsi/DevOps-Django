from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import app1_db


def hello1(request):
    return HttpResponse("Hello Python!")

def hello2(request):
    return HttpResponse("Hello Django!")

def htmlexample(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

def htmlportfolio(request):
    template = loader.get_template('myportfolio.html')
    return HttpResponse(template.render())

def htmlstaticportfolio(request):
    template = loader.get_template('staticportfolio.html')
    return HttpResponse(template.render())

def htmlresume(request):
    template = loader.get_template('myresume.html')
    return HttpResponse(template.render())

def db_table(request):
    mymembers = app1_db.objects.all().values()
    template = loader.get_template('db.html')
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context,request))

def db_dict(request):
    mymembers = app1_db.objects.all().values()
    output = " "
    for x in mymembers:
        output += x["firstname"] + x["lastname"]
    return HttpResponse(output)

def db_add(request):
    template = loader.get_template('add.html')
    return HttpResponse(template.render({}, request))

def db_addrecord(request):
    x = request.POST['first']
    y = request.POST['last']

    db = app1_db(firstname = x,lastname = y)
    db.save()
    return HttpResponseRedirect(reverse('db_table'))

def db_delete(request,id):
    dele=app1_db.objects.get(id=id)
    dele.delete()
    return HttpResponseRedirect(reverse('db_table'))

def db_update(request,id):
    mymember = app1_db.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {
        'mymember' : mymember,
    }
    return HttpResponse(template.render(context,request))

def db_updaterecord(request,id):
    x = request.POST['first']
    y = request.POST['last']

    upd=app1_db.objects.get(id=id)
    upd.firstname = x
    upd.lastname = y
    upd.save()
    return HttpResponseRedirect(reverse('db_table'))