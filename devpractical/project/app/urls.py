from django.urls import path
from . import views
urlpatterns=[
    path("a/",views.hello1,name='hello1'),
    path("b/",views.hello2,name='hello2'),
    path("c/",views.htmlexample,name='htmlexample'),
    path("d/",views.htmlportfolio,name='htmlportfolio'),
    path("portfolio/",views.htmlstaticportfolio,name='htmlstaticportfolio'),
    path("resume/",views.htmlresume,name='htmlresume'),
    path("db/",views.db_dict,name='db_dict'),
    path("dbt/",views.db_table,name='db_table'),
    path("dbt/add/",views.db_add,name='db_add'),
    path("dbt/add/addrecord/",views.db_addrecord,name='db_addrecord'),
    path("dbt/delete/<int:id>",views.db_delete,name="db_delete"),
    path("dbt/update/<int:id>",views.db_update,name='db_update'),
    path("dbt/update/updaterecord/<int:id>",views.db_updaterecord,name='db_updaterecord'),

]