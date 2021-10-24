from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form, name='form'),
    path('add', views.add, name='add'),
    path('set_as_done', views.set_as_done, name='set_as_done')
]