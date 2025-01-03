# ANGRY TEST
### Django проект с авторизацией через Telegram-бота

## Требования к проекту:
- [x] Создать веб-страницу с кнопкой "Войти через Telegram"  
- [x] При нажатии на кнопку происходит перенаправление в Telegram-бота, где ссылка содержит команду /start с уникальным токеном  
- [x] После отправки команды пользователем Django получает токен и связывает Telegram-аккаунт с пользователем веб-сайта  
- [x] Веб-страница автоматически обновляется, отображая имя или никнейм пользователя из Telegram. Пользователь авторизуется через стандартные механизмы Django.  


## В проекте используется:
- `Python 3.12` как основной язык приложения.
- `Django 4.2.17` в качестве фреймворка.
- `Telebot` для настройки телеграм бота.
- `uuid` для создания уникального токена.


## Дополнительная информация:
- В `settings.py` для временного удобства отключена валидация паролей.


## Реализация
- DJANGO проект с приложением:
  - angry_app;
  - users;
- Расширенная модель `User`, дополнена полями:
  - telegram_id`;
  - token;
- Представления (views) в `angry_app`:
  - index;
  - my_page;
- Представления (views) в `users`:
  - login;
  - logout;
  - register;
- Telegram bot с командами:
  - /start


## Переменные окружения
- DJANGO_SECRET_KEY - ключ DJANGO приложения;
- TELEGRAM_BOT_TOKEN - токен бота в Telegram;
- TELEGRAM_BOT_NAME - имя бота в Telegram;
- DOMAIN - домен сайта;

## Скриншоты
Прилогается папка `screenshots` со скриншотами, демонстрирующими работу проекта.
- `Step 1.png` ГЛАВНАЯ СТРАНИЦА: 
  - При нажатии на `моя страница`, вместо `my_page` перенаправит на `страницу входа`.

- `Step 2.png` СТРАНИЦА ВХОДА. На выбор:
  - Вход при помощи `логин + пароль`;
  - Регистрация нового пользователя;
  - Вход через телеграм (выбираем этот способ и жмём на кнопку);
  
- `Step 3.png` TELEGRAM BOT: 
  - Нажимаем на кнопку `ЗАПУСТИТЬ` или вводим команду `/start`
  - При успешном входе, переходим по ссылке обартно на сайт.
  
- `Step 4.png` ГЛАВНАЯ СТРАНИЦА:
  - Попадаем на `главную страницу`;
  - Справа вверху будет ваше имя указанное в Telegram или `Telegram ID`;
  - Жмём на кнопку `МОЯ СТРАНИЦА`;
  
- `Step 5.png` МОЯ СТРАНИЦА:
  - Попадаем на `мою страницу`.
  - Теперь мы имеем доступ к данной странице.


## Установка
```bash
$ python -m venv venv  
$ source venv/Scripts/activate  
$ python -m pip install --upgrade pip  
$ pip install -r requirements.txt  
$ python manage.py migrate  
$ python manage.py runserver

(another terminal)
$ source venv/Scripts/activate  
$ python manage.py angry_bot
```
### Перейти по http://127.0.0.1:8000/



