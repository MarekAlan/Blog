import pytest
from django.contrib.auth.models import User

from blog_app.models import Blog, Post


@pytest.fixture  # fixtura ktora tworzy urzytkownikow do testow bo bd testow jest pusta na poczatku
def users():
    users = []
    for x in range(10):  # tworzymy 10 userow do spradzenia bazy danych
        u = User.objects.create(username=x)
        users.append(u)
    return users


@pytest.fixture
def blogs(users):  # bo blogi maja authorow a autorzy to users
    blogs = []
    for user in users:  # dla każdego usera ktorego fixtura stworzyla
        for x in range(3):  # kazdy user tworzy 3 blogi
            b = Blog.objects.create(
                name='x', topic='x', author=user
            )
            blogs.append(b)
    return blogs


@pytest.fixture
def posts(blogs):  # post jest przypisany do bloga ktory ma autora
    posts = []
    for blog in blogs:
        for x in range(3):
            p = Post.objects.create(
                title='x', text='x', blog=blog
            )
            posts.append(p)
    return posts


@pytest.fixture  # tworzymy 1 usera na potrzeby logowania
def user():
    return User.objects.create(username='yoda')
