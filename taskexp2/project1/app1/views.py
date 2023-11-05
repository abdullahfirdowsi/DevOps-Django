#from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Book,Student,Product,Order,Productdetail
# Create your views here.
def book(request):
    myBook=Book.objects.all()
    template=loader.get_template('publications.html')
    context={
        'myBook':myBook
    }
    return HttpResponse(template.render(context,request))
def student(request):
    Studentdb = Student.objects.all()
    template = loader.get_template('student.html')
    context = {
        'Studentdb' : Studentdb,
    }
    return HttpResponse(template.render(context, request))
def product(request):
    Productdb = Product.objects.all()
    template = loader.get_template('product.html')
    context = {
        'Productdb' : Productdb,
    }
    return HttpResponse(template.render(context, request))
def order_list(request):
    Orderdb = Order.objects.all()
    template = loader.get_template('order.html')
    context = {
        'Orderdb' : Orderdb,
    }
    return HttpResponse(template.render(context, request))
def product_details(request):
    Pgdb = Productdetail.objects.all()
    template = loader.get_template('product details.html')
    context = {
        'Pgdb' : Pgdb,
    }
    return HttpResponse(template.render(context, request))