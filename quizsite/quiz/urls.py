from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = "index"),
    path('level<int:num>/', views.level, name = "level"),
    path('score/', views.score, name = "score"),
]