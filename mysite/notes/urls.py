from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    # ex: /notes/
    path('', views.index, name='index'),
    # ex: /notes/add/
    path('add/', views.add, name='add'),
]