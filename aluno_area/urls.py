from django.conf.urls import url

from . import views

app_name = 'aluno_area'
urlpatterns = [
    url(r'^index', views.index, name='index'),
]