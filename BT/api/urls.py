from django.urls import path
from . import views


urlpatterns = [
    path('',views.getarticles),
    path('articles/', views.getArticles),
    path('articles/<str:pk>', views.getArticles),
]
