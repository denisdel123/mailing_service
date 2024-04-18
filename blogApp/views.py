
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from transliterate import translit

from blogApp.forms import BlogForm
from blogApp.models import Blog


class BlogCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Blog
    permission_required = 'blogApp.add_blog'
    form_class = BlogForm
    success_url = reverse_lazy('blogApp:list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)


class BlogListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Blog
    permission_required = 'blogApp.view_blog'

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_published=True)
        return queryset


class OwnerBlogListView(ListView):
    model = Blog

    def get_queryset(self):
        user_id = self.request.user.pk
        queryset = super().get_queryset().filter(owner_id=user_id)
        return queryset


class BlogDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Blog
    permission_required = 'blogApp.view_blog'

    def get(self, request, *args, **kwargs):
        blog = self.get_object()
        blog.view_count += 1
        blog.save()

        return super().get(request, *args, **kwargs)

    def create_slag(self, title):
        return translit(title, 'ru', reversed=True)

    def get_queryset(self):
        queryset = super().get_queryset()

        for blog in queryset:
            blog.slug = self.create_slag(blog.title)
            blog.save()
        return queryset

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('blogApp:detail', kwargs={'pk': object_id})
        return detail_url


class BlogUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Blog
    permission_required = 'blogApp.change_blog'

    form_class = BlogForm

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('blogApp:detail', kwargs={'pk': object_id})
        return detail_url


class BlogDeleteView(DeleteView):
    model = Blog


def publication(request, pk):
    if request.method == 'POST':
        obj = get_object_or_404(Blog, pk=pk)
        if obj.is_published is not True:
            obj.at_published = timezone.now()
        obj.is_published = not obj.is_published
        obj.save()
        return redirect('blogApp:detail', pk=pk)
