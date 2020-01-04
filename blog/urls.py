from django.urls import path

from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.IndexListView.as_view(), name='index'),
    path('add_post/', views.add_post, name='add_post'),
    path('tag/<tag_name>/', views.TagListView.as_view(), name='tag'),
]
