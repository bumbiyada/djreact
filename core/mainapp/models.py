from django.db import models
from django.utils import timezone

# Create your models here.


class ListAll(models.Model):
    Foiv = models.CharField(
        verbose_name='ФОИВ',
        max_length=64)
    Document_type = models.CharField(
        verbose_name='Тип документа',
        max_length=64)
    Document_number = models.CharField(
        verbose_name='Номер документа',
        max_length=64)
    Document_init_data = models.DateTimeField(
        verbose_name='Дата создания документа',
        auto_now=False,
        auto_now_add=False,
        default=timezone.now)
    STAGE_TYPES = (
        (1, 'Аннулирование'),
        (2, 'Внесение остатка/выдача перерасхода'),
        (3, 'Выгрузка'),
        (4, 'Отражение в учете'),
        (5, 'Регистрация в учете'),
        (6, 'Согласование'),
        (7, 'Установка статуса выгрузки'),
        (8, 'Утверждение'),
        (9, 'Формирование'),
        (10, 'Формирование и выгрузка'),
        (11, 'Формирование отправки'),
    )
    Stage_name = models.IntegerField(
        verbose_name='Этап',
        choices=STAGE_TYPES
    )
    Stage_data = models.DateTimeField(
        verbose_name='Дата проведения этапа',
        auto_now=False,
        auto_now_add=False,
        default=timezone.now
    )
    Stage_user = models.CharField(
        verbose_name='Исполнитель',
        max_length=64
    )
    Is_aborted = models.BooleanField(
        verbose_name='Прервана',
        default=False
    )
    Is_done = models.BooleanField(
        verbose_name='Выполнена',
        default=True
    )
    Marked_on_delete = models.BooleanField(
        verbose_name='Пометка на удаление',
        default=False
    )

    def __str__(self):
        name = str(self.Document_number) + ' ' + str(self.Stage_name) + ' ' + str(self.Stage_data)
        return name
