from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy

from blog.models import Blog


class BlogListView(ListView):
    model = Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'content', 'image')
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form, *args, **kwargs):
        new_blog = form.save(commit=False)
        new_blog.owner = self.request.user
        new_blog.save()
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object
