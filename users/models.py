from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    telegram_id = models.PositiveBigIntegerField(verbose_name='TELEGRAM ID пользователя',
                                                 db_index=True,
                                                 null=True)
    token = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.username or f'Telegran ID: {self.telegram_id}'
