
from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('login/', login_views, name='login_view'),
    path('register/', register_views, name='register_views'),

]
