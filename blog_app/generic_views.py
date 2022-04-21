from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from blog_app.models import Post


class CreatePostView(CreateView):
    model = Post
    fields = '__all__'
    # success_url = reverse_lazy('index')
    template_name = 'form.html'


class DetailPostVIew(DetailView):
    model = Post
    template_name = 'gpv.html'
