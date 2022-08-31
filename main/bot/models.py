from django.db import models


class BotUser(models.Model):
    id = models.BigIntegerField(primary_key=True,
                                unique=True,
                                null=False,
                                blank=False)
    username = models.TextField(blank=False,
                                null=False)
    payment = models.BooleanField(default=False,
                                  null=False)

    class Meta:
        verbose_name = 'Пользователь бота'
        verbose_name_plural = 'Пользователи бота'
