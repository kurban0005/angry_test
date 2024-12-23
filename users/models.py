from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    telegram_id = models.PositiveBigIntegerField(verbose_name='TELEGRAM ID пользователя',
                                                 db_index=True,
                                                 null=True)

    def __str__(self):
        return self.telegram_id


# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     telegram_id = models.PositiveBigIntegerField(verbose_name='TELEGRAM ID пользователя',
#                                                  db_index=True,
#                                                  null=True)
#
#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Profile.objects.create(user=instance)
#
#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.profile.save()
