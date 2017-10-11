from django.conf.urls import url
from django.contrib import admin
from converter import views

urlpatterns = [

    url(r'^', view=views.converter,name='converter'),
    url(r'^download/', view=views.download,name='download'),
]
