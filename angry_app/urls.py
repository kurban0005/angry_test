from django.urls import path
from . import views

app_name = 'angry_app'
urlpatterns = [
    # Домашняя страница.
    path('', views.index, name='index'),
    # Моя страница
    path('my_page/', views.my_page, name='my_page'),

]
