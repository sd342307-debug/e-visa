"""eVisa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from visa.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('login',login,name='login'),
    path('admin_home',admin_home,name='admin_home'),
    path('user_home',user_home,name='user_home'),
    path('logout',logout,name='logout'),
    path('signup',signup,name='signup'),
    path('users',users,name='users'),
    path('delete_user/<int:id>',delete_user,name='delete_user'),
    path('apply',apply,name='apply'),
    path('my_visa',my_visa,name='my_visa'),
    path('all_visa',all_visa,name='all_visa'),
    path('change_status/<int:id>',change_status,name='change_status'),
    path('delete_visa/<int:id>',delete_visa,name='delete_visa'),
    path('delete_my_visa/<int:id>',delete_my_visa,name='delete_my_visa'),
    path('pay_now/<int:id>',pay_now,name='pay_now'),
    path('feedback',feedback,name='feedback'),
    path('view_feedback',view_feedback,name='view_feedback'),
    path('delete_feedback/<int:id>',delete_feedback,name='delete_feedback'),
    path('edit_profile',edit_profile,name='edit_profile'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
