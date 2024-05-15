from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . import views
from django.conf.urls.static import static 



urlpatterns = [
    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('blog',views.blog,name="blog"),
    path('contact',views.contact,name="contact"),
    path('category',views.category,name="category"),
    path('extra/<str:slug>/',views.single,name="single"),
    path('<str:sno>/',views.my_single,name="my_single"),
    path('signupForm_view', views.signupForm_view, name="signupForm_view"),
    path('login_view', views.login_view, name="login_view"),
    path('logout_view', views.logout_view, name="logout_view"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 