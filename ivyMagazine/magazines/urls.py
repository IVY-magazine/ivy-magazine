from django.urls import path
from django.conf.urls import include, url
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('blog/', views.blog, name="blog"),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('magazine/', views.magazine, name="magazine"),
    path('aboutUs/', views.aboutUs, name="aboutUs"),
    path('contactUs/', views.contactUs, name="contactUs"),
    path('info/', views.info, name='info'),
    url(r'^mediumBlog/', TemplateView.as_view(template_name="medium.com/@ivisualizeyou"),
                   name='mediumBlog'),
]