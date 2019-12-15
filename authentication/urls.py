from django.urls import path, include


app_name = 'authentication'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]
