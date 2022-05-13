from django.db import models


class Subjects(models.Model):

    ''' Модель описывающая тему задающего вопрос на форуме '''

    user_name = models.CharField(max_length=50, verbose_name='Пользователь')
    title = models.CharField(max_length=150, unique=True, verbose_name='Вопрос')
    content = models.TextField(null=True, blank=True, verbose_name='Описание вопроса')
    media_files = models.FileField(null=True, blank=True, verbose_name='Медиа-вложения')
    published = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Темы вопросов'
        verbose_name = 'Тема вопроса'
        ordering = ['-published']


class Comments(models.Model):

    ''' Модель описывающая комментарий к конкретному вопросу '''

    user_name_comm = models.CharField(max_length=50, verbose_name='Пользователь-комментатор')
    content_comm = models.TextField(null=True, blank=True, verbose_name='Текст комментария')
    media_files_comm = models.FileField(null=True, blank=True, verbose_name='Медиа-вложения комментария')
    published_comm = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации комментария')
    subject = models.ForeignKey('Subjects', on_delete=models.CASCADE, verbose_name='Вопрос')

    def __str__(self):
        return f'Коммент от {str(self.published_comm)[:19]} -- {self.content_comm[:10]}...'

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
        ordering = ['-published_comm']


class Rubric(models.Model):

    ''' Модель описывающая общую тематику вопросов '''

    name = models.CharField(max_length=60, db_index=True, verbose_name='Тематика вопросов')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Список тематик'
        verbose_name = 'Тематика вопроса'
        ordering = ['name']

