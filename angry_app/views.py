from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    '''Домашняя страница.'''
    return render(request, 'angry_app/index.html')


@login_required()
def my_page(request):
    '''Моя страница.'''
    return render(request, 'angry_app/my_page.html')
