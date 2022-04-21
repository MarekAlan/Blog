from audioop import reverse

import self as self
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View

from blog_app.forms import AddPostForm, AddPostFromBlogForm, AddPostModelForm, AddCommentModelForm
from blog_app.models import Blog, Post, Comment


class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


class IndexView2(View):

    def get(self, request):
        return render(request, 'cosnowego.html')


class AddBlogView(LoginRequiredMixin, View):  # to jest tylko dla zalogowanych - w () na maksa w lewo

    def get(self, request):
        return render(request, 'add_blog.html')

    def post(self, request):
        name = request.POST['name']
        topic = request.POST['topic']
        Blog.objects.create(name=name, topic=topic, author=request.user)  # po to aby był jakiś autor bloga
        return redirect('show_blogs')


class AddPostView(View):

    def get(self, request):
        form = AddPostForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AddPostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            blog = form.cleaned_data['blog']
            Post.objects.create(text=text, blog=blog)
            return redirect('add_post')
        return render(request, 'form.html', {'form': form})


class ShowBlogView(View):

    def get(self, request):
        return render(request, 'list.html', {'object_list': Blog.objects.all()})


class ShowPostView(View):

    def get(self, request):
        return render(request, 'list.html', {'object_list': Post.objects.all()})


class ShowDetailBlog(View):

    def get(self, request, id):
        form = AddPostModelForm()
        blog = Blog.objects.get(pk=id)
        return render(request, "blog_detail.html", {'blog': blog, 'form': form})

    def post(self, request, id):
        blog = Blog.objects.get(pk=id)
        form = AddPostModelForm(request.POST)
        if form.is_valid():
            # text = form.cleaned_data['text']           #to jest sposób na piechote
            # Post.objects.create(text=text, blog=blog)
            post = form.save(commit=False)  # a to jest automatczny zaciagajacy z ModelForm
            post.blog = blog  # jak by nie zrobić commit=False to by spróbował zapisać i by sie wywalil
            post.save()  # teraz juz wie gdzie zapisac bo juz wie ze to blog
            return redirect(f'/blog_app/blog/{blog.id}/')
        return render(request, 'form.html', {'form': form})


class ShowDetailPost(View):

    def get(self, request, id):
        post = Post.objects.get(pk=id)
        return render(request, "post_detail.html", {'post': post})


class UpdatePostView(View):

    def get(self, request, id):
        post = Post.objects.get(pk=id)
        form = AddPostModelForm(instance=post)
        return render(request, "form.html", {'form': form})

    def post(self, request, id):
        post = Post.objects.get(pk=id)
        form = AddPostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('update_post'), args=[id])
        return render(request, "form.html", {'form': form})


class DeletePostView(View):

    def get(self, request, id):
        post = Post.objects.get(pk=id)
        return render(request, "form.html", {})

    def post(self, request, id):
        post = Post.objects.get(pk=id)
        post.delete()
        return redirect("show_post")


class AddCommentView(LoginRequiredMixin, View):

    def get(self, request):
        form = AddCommentModelForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AddCommentModelForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return redirect('index')
        return render(request, 'form.html', {'form': form})


class CommentsView(View):

    def get(self, request, id):
        comment = Comment.objects.get(pk=id)
        form = AddCommentModelForm(instance=comment)
        return render(request, 'form.html', {'form': form})

    def post(self, request, id):
        comment = Comment.objects.get(pk=id)
        form = AddCommentModelForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('index')
        return render(request, "form.html", {'form': form})
