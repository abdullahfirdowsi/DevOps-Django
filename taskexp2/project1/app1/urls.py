from django.urls import path
from .import views
urlpatterns=[
    path('book/',views.book,name='book'),
    path('student/',views.student,name='student'),
    path('product/',views.product,name='product'),
    path('order/',views.order_list,name='order'),
    path('product_details/',views.product_details,name='product_details'),
]