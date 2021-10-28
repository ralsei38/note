from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('form', views.form, name='form'),
    path('add', views.add, name='add'),
    path('set_as_done/<int:id>', views.set_as_done, name='set_as_done'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('done', views.done, name='done'),
    path('categories', views.categories, name='categories')
]