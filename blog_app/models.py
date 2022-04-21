from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse


class Blog(models.Model):
    name = models.CharField(max_length=64)
    creation_date = models.DateTimeField(auto_now_add=True)
    topic = models.CharField(max_length=64)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("show_detail_blog",
                       args=(self.id,))  # reverse działa jak url - czyli szuka po podanej nazwie w kodzie
        # args musi być krotką więc zostawiamy , i puste


class Post(models.Model):
    title = models.CharField(max_length=64, default="")
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.text[:30]} {self.creation_date}'  # pierwsze 30 znaków

    def get_absolute_url(self):
        return reverse("show_detail_post", kwargs={'id': self.id})  # kwargs to podobne co args ale musi być słownikiem
        # keyword argument

    def get_update_url(self):
        return reverse("update_post", kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse("delete_post", kwargs={'id': self.id})


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    nick = models.CharField(max_length=10)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
