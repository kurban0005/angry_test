from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from dotenv import load_dotenv
# from django.contrib.auth.models import User
from django.conf import settings
import telebot
import os

load_dotenv()

bot = telebot.TeleBot(os.getenv('TELEGRAM_BOT_TOKEN'))


def login_view(request):
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
        context = {'BOT_NAME': os.getenv("TELEGRAM_BOT_NAME")}
        return render(request, 'users/login.html', context)


def logout_view(request):
    logout(request)
    return render(request, 'angry_app/index.html')


def register(request):
    '''Регистрирует нового пользователя.'''
    if request.method != 'POST':
        # Выводит пустую форму регистрации
        form = UserCreationForm()
    else:
        # Обработка данных
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу
            login(request, new_user)
            return redirect('angry_app:index')
    # Вывести пустую и недействительную форму
    context = {'form': form}
    return render(request, 'users/register.html', context)
