from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog.models import Blog


# Create your views here.
class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'text', 'image', 'slug')
    success_url = reverse_lazy('blog_list')


class BlogListView(ListView):
    model = Blog
    fields = ('title', 'text')

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        # queryset = queryset.filter(to_publish=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    fields = ('title', 'text', 'image', 'created_at', 'views')


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'text', 'image')
    success_url = reverse_lazy('blog_detail')


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')
