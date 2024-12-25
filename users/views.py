from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from dotenv import load_dotenv
from .forms import RegisterForm
from users.models import User
import uuid
import telebot
import os

load_dotenv()


def login_view(request):
    '''Авторизует пользователя'''
    if request.user.is_authenticated:
        return redirect('angry_app:index')
    token = request.COOKIES.get('token')
    if token is None:
        token = str(uuid.uuid4())
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = redirect('angry_app:index')
            return response
        else:
            context = {'error': True}
            return render(request, 'users/login.html', context)
    else:
        token = request.COOKIES.get('token')
        if token is None:
            token = str(uuid.uuid4())
        else:
            user = User.objects.filter(token=token).first()
            if user:
                login(request, user)
                response = redirect('angry_app:index')
                response.delete_cookie('token')  # Удалить существующий куки
                return response
        context = {'TELEGRAM_BOT_NAME': os.getenv("TELEGRAM_BOT_NAME"), 'token': token}
        response = render(request, 'users/login.html', context)
        response.set_cookie('token', token, max_age=60 * 60 * 12)  # Ставим куки на 12 часов
        return response


def logout_view(request):
    logout(request)
    response = render(request, 'angry_app/index.html')
    return response


def register(request):
    '''Регистрирует нового пользователя.'''
    # if request.method != 'POST':
    #     form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('angry_app:index')
    else:
        form = RegisterForm()
        # Вывести пустую и недействительную форму
        context = {'form': form}
        return render(request, 'users/register.html', context)
