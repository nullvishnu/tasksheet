from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from user.controller import usercontroller

urlpatterns = [
    path('', usercontroller.login_index),
    path('signup/', usercontroller.signup_index),
    path('userdata', usercontroller.user_fetch),
    path('userlogin', usercontroller.user_login),
    path('dashboard', usercontroller.dashboard_index),
    path('task', usercontroller.task_fetch)
]