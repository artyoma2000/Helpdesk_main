from django.urls import path
from . import views

urlpatterns = [
    path('', views.create, name='create'),
    path('news_home', views.news_home, name='news_home')
]
