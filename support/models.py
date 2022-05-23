from django.db import models


class OfferMessage(models.Model):

    ''' Класс модели замечаний и предложений по сайту...'''

    choices_category = (
        (None, 'Выберите категорию'),
        ('authorization', 'Проблема авторизации'),
        ('url_error', 'Перенаправление по неверному адресу'),
        ('other', 'Другое')
    )

    name_of_user = models.CharField(max_length=50, verbose_name='Пользователь')
    category = models.CharField(max_length=50, choices=choices_category, verbose_name='Категория')
    media_files = models.FileField(null=True, blank=True, verbose_name='Медиа-вложения')
    content = models.TextField(null=True, blank=True, verbose_name='Описание вопроса')
    sent = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата отправления сообщения')
    reviewed = models.BooleanField(default=False, verbose_name='Принято к исправлению')
    fixed = models.BooleanField(default=False, verbose_name='Исправлено')

    class Meta:
        verbose_name_plural = 'Замечания/Предложения'
        verbose_name = 'Замечание/Предложение'
        ordering = ['-sent']
