from django.urls import path

from blogApp.apps import BlogappConfig
from blogApp.views import BlogCreateView

app_name = BlogappConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
]