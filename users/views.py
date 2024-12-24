from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.conf import settings

from .forms import RegisterForm
from dotenv import load_dotenv
from users.models import User

import uuid
import telebot
import os

load_dotenv()


def login_view(request):
    if request.user.is_authenticated:
        return redirect('angry_app:index')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('angry_app:index')
        else:
            context = {'error': True}
            return render(request, 'users/login.html', context)
    else:
        token = request.COOKIES.get('token')
        context = {}
        if token is None:
            token = str(uuid.uuid4())
        else:
            user = User.objects.filter(token=token).first()
            if user:
                login(request, user)

        context = {'TELEGRAM_BOT_NAME': os.getenv("TELEGRAM_BOT_NAME"), 'token': token}

        response = render(request, 'users/login.html', context)
        response.set_cookie('token', token, max_age=60 * 60 * 12)  # Ставим куки на 12 часов
        return response


def logout_view(request):
    logout(request)
    response = render(request, 'angry_app/index.html')
    # response.delete_cookie("token")
    return response


def register(request):
    '''Регистрирует нового пользователя.'''
    if request.method != 'POST':
        # Выводит пустую форму регистрации
        form = RegisterForm()
    else:
        # Обработка данных
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу
            login(request, new_user)
            return redirect('angry_app:index')
    # Вывести пустую и недействительную форму
    context = {'form': form}
    return render(request, 'users/register.html', context)
