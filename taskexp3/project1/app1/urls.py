from django.urls import path
from .import views 
urlpatterns=[
    path('todo/',views.todo,name='todo'),
    path('calculator/',views.calculator,name='calculator')  
]