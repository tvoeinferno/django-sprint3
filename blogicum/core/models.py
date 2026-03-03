from django.db import models

from core.constants import MAX_LENGTH


class PublishedModel(models.Model):
    is_published = models.BooleanField(
        'Опубликовано',
        default=True,
        help_text='Снимите галочку, чтобы скрыть публикацию.')

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)

    class Meta:
        abstract = True


class TitleModel(models.Model):
    title = models.CharField('Заголовок', max_length=MAX_LENGTH)

    class Meta:
        abstract = True
