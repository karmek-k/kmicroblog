from django.urls import path, include

from . import views


app_name = 'authentication'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('signup', views.signup, name='signup'),
]
