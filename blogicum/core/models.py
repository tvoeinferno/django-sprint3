from django.db import models

from core.constants import MAX_NAME_LENGTH


class IsPublishedAbstract(models.Model):
    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )

    class Meta:
        abstract = True


class CreatedAtAbstract(models.Model):
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        abstract = True


class TitleAbstract(models.Model):
    title = models.CharField('Заголовок', max_length=MAX_NAME_LENGTH)

    class Meta:
        abstract = True
