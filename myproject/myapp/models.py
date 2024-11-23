from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    patronymic = models.CharField(verbose_name='Отчество', max_length=120)
    phone = models.CharField(verbose_name='Телефон', max_length=12)

    def __str__(self):
        return self.username


class Orders(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('CustomUser', verbose_name='Автор', related_name='orders_customuser',
                              on_delete=models.CASCADE)
    status = models.ForeignKey('Status', verbose_name='Статус', related_name='orders_status', on_delete=models.CASCADE)
    phone = models.CharField(verbose_name='Номер машины', max_length=8)
    orderdatetime = models.DateTimeField(blank=True, null=True)
    description= models.CharField(verbose_name='Описание нарушения',max_length=200)


    def __str__(self):
        return str(self.created)

    class Meta:
        ordering = ['created']
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'


class Status(models.Model):
    title = models.CharField(verbose_name='Статус', max_length=60)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'




