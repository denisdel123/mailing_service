from django.urls import path

from blogApp.apps import BlogappConfig
from blogApp.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, OwnerBlogListView, \
    BlogDeleteView, publication

app_name = BlogappConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('list/', BlogListView.as_view(), name='list'),
    path('my/list/', OwnerBlogListView.as_view(), name='my_list'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),

    path('publication/<int:pk>', publication, name='publication'),
]