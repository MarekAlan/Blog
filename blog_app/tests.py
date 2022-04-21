import pytest
from django.contrib.auth.models import User
from django.test import Client
from django.urls import reverse

# @pytest.mark.django_db        # ten dekorator wbija do bazy danych i tworzy swoja pusta na potrzebe testu
# def test_ala_ma_kota():       # pusty test ktory sprawdza czy wogole dziala,
#     assert True               # czy sa biblioteki, czy dobrze jest pytest.ini
# musi byc słowo test. def test_......
from blog_app.models import Blog, Post


@pytest.mark.django_db
def test_check_index():
    # Client symuluje przeglądarke
    client = Client()  # otwieramy naszą przeglądarke, udajemy przegladarke
    url = reverse('index')  # tworzymy sobie url na którego chcemy wejść
    response = client.get(url)  # wejdz na adres url i wynik wejscia zapisz do zmiennej response
    assert response.status_code == 200  # status_code 200 znaczy ze wszystko dziala


@pytest.mark.django_db
def test_user_list(users):  # poszukaj w pliku conftest.py funkcje users i ja odpala i tworzy liste 10 userow
    client = Client()  # czyli dodajemy fixtura userow na potrzeby testu bo baza jest pusta na poczatku
    url = reverse('userlist')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(users)  # class UserListView(ListView) zwraca object_list
    for user in users:
        assert user in response.context['object_list']


@pytest.mark.django_db
def test_blog_list(blogs):  # fixtura blogs
    client = Client()
    url = reverse('show_blogs')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(blogs)
    for blog in blogs:
        assert blog in response.context['object_list']


@pytest.mark.django_db
def test_post_list(posts):  # fixtura posts zaciaga blogs i users
    client = Client()
    url = reverse('show_post')
    response = client.get(url)
    assert response.status_code == 200
    assert response.context['object_list'].count() == len(posts)
    for post in posts:
        assert post in response.context['object_list']


@pytest.mark.django_db
def test_check_blog_add_get_not_login():
    client = Client()
    url = reverse('add_blog')
    response = client.get(url)
    assert response.status_code == 302  # status_code 302 przekierowuje na inna strone w naszym przypadku do logowania


@pytest.mark.django_db
def test_add_blog(user):  # sprawdzamy czy sie udalo zalogowac ale funkcja get
    url = reverse('add_blog')  # czy ten widok jest dostepny tylko dla zalogowanego
    client = Client()
    client.force_login(user)  # ten klient sie loguje bez hasła bo tak mu mówimy
    response = client.get(url)  # wchodzimy na getem na wybrany url
    assert response.status_code == 200  # poprzednio było 302 bo sie nie logowal


@pytest.mark.django_db
def test_add_blog(user):  # teraz post po zalogowaniu
    url = reverse('add_blog')
    client = Client()
    client.force_login(user)
    d = {
        'name': 'a',
        'topic': 'bb'
    }
    response = client.post(url, d)  # bo post przesyla słownik z formularzy we views
    assert response.status_code == 302  # bo w funkcja class AddBlogView jak uda sie post to jest redirect
    Blog.objects.get(name='a', topic='bb')  # jezeli pobierze 1 element to bedzie ok, inaczej bedzie blad
    # assert nie potrzebny bo i tak tylko 1 objekt


@pytest.mark.django_db
def test_register_user():
    url = reverse('register')
    client = Client()
    d = {
        'username': 'alan',
        'pass1': 'bb',
        'pass2': 'bb'
    }
    response = client.post(url, d)
    assert response.status_code == 302
    User.objects.get(username='alan')  # sprawdzamy czy stworzyl sie user
    assert client.login(username='alan', password='bb')  # sprawdzamy czy udaje sie zalogowac


@pytest.mark.django_db
def test_add_post_with_blog(blogs):
    url = reverse('add_post')
    client = Client()
    d = {
        'text': 'aaa',
        'blog': blogs[0].id  # bierzemy id 1 pierwszego bloga w blogs
    }
    response = client.post(url, d)
    assert Post.objects.first()  # to samo co get tylko bierzemy 1 element
