from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_post/', views.add_post, name='add_post'),
    path('tag/<tag_name>', views.tag, name='tag'),
]
