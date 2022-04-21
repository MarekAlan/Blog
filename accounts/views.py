from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from django.views.generic import ListView

from accounts.forms import LoginFormView, CreateUserForm, UserPermUpdateForm


class LoginView(View):

    def get(self, request):
        form = LoginFormView()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = LoginFormView(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username,
                                password=password)  # tu mu mówimy zautentykuj mi dane osobowe czy sa w bazie.
            if user is not None:  # Jezeli jest w bazie to bedzie None
                login(request, user)  # wywołujemy funkcje login dla danego usera
                return redirect('index')  # jezeli sie zalogowalo to nas wysyla do 'index'
        return render(request, 'form.html', {'form': form})  # jezeli się nie zalogowało to nas przesyla tu


class RegisterView(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(
                form.cleaned_data['pass1'])  # trzeba to zrobić aby był prawdziwy password - inaczej nie działa
            user.save()
            return redirect('login')
        return render(request, 'form.html', {'form': form})


class LogOutView(View):

    def get(self, request):
        logout(request)
        return redirect('index')


class UserListView(ListView):
    model = User
    template_name = 'accounts/user_list_view.html'


class UserPermSetting(UserPassesTestMixin, View):

    def test_func(self):
        return self.request.user.is_superuser

    def get(self, request, id):
        user = User.objects.get(pk=id)
        form = UserPermUpdateForm(instance=user)
        return render(request, 'form.html', {'form': form})

    def post(self, request, id):
        user = User.objects.get(pk=id)
        form = UserPermUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
        return render(request, 'form.html', {'form': form})
