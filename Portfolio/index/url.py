from django.urls import path
from index import views



urlpatterns = [
    path('', views.index, name='index'),
    path('blog_single/', views.blog_single, name='blog_single'),
]