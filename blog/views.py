from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Blog


# Create your views here.
class BlogCreateView(CreateView):
    model = Blog
    fields = ('title', 'text', 'image')
    success_url = reverse_lazy('blog_list')

    def form_valid(self, form):
        if form.is_valid():
            new = form.save()
            new.slug = slugify(new.title)
            new.save()
        return super().form_valid(form)


class BlogListView(ListView):
    model = Blog
    fields = ('title', 'text')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(to_publish=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    fields = ('title', 'text', 'image', 'created_at', 'views')

    def get_object(self, queryset=None):
        obj = super().get_object()
        obj.views += 1
        if obj.views == 100:
            send_mail(
                subject='Уведомление о достижении',
                message='Поздравляем! Статья набрала 100 просмотров в блоге.',
                from_email='reaver74@yandex.ru',
                recipient_list=['reaver_std@mail.ru'],
                fail_silently=False
            )
        obj.save()
        return obj


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ('title', 'text', 'image')

    def form_valid(self, form):
        if form.is_valid():
            new = form.save()
            new.slug = slugify(new.title)
            new.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog_detail', args=[self.object.slug])


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog_list')


def toggle_active(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    if blog.to_publish:
        blog.to_publish = False
    else:
        blog.to_publish = True
    blog.save()
    return redirect('blog_detail', slug=blog.slug)
