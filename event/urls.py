"""event URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from infinity import views as inf_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inf_views.home,name='home'),
    path('login/', inf_views.admin,name='login'),
    path('del_usr/', inf_views.del_usr,name='del_usr'),
    path('del_eve/', inf_views.del_eve,name='del_eve'),
    path('find_usr/', inf_views.find_usr,name='find_usr'),
    path('disp_user/', inf_views.find_usr,name='disp_user'),
    path('syslog/', inf_views.syslog,name='syslog'),
    path('updatedata/', inf_views.updatedata,name='updatedata'),
    path('change_password/', inf_views.updatepass,name='updatepass'),
]
