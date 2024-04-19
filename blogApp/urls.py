from django.urls import path
from django.views.decorators.cache import cache_page

from blogApp.apps import BlogappConfig
from blogApp.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, OwnerBlogListView, \
    BlogDeleteView, publication

app_name = BlogappConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('list/', cache_page(60)(BlogListView.as_view()), name='list'),
    path('my/list/', cache_page(60)(OwnerBlogListView.as_view()), name='my_list'),
    path('detail/<int:pk>', BlogDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BlogDeleteView.as_view(), name='delete'),

    path('publication/<int:pk>', publication, name='publication'),
]