from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('magazine/', views.magazine, name="magazine"),
    path('aboutUs/', views.aboutUs, name="aboutUs"),
    path('contactUs/', views.contactUs, name="contactUs"),
    path('info/', views.info, name='info'),
]