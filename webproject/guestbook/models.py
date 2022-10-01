from django.db import models
from django.db.models import TextChoices



class StatusChoices(TextChoices):
    ACTIVE = 'active', 'Активно'
    BLOCKED = 'blocked', 'Заблокировано'


class Guest(models.Model):
    author_name = models.CharField(
        verbose_name = 'Имя автора',
        max_length = 30,
        null = False,
        blank = False
    )
    author_email = models.EmailField(
        verbose_name = 'Почта автора',
        max_length = 50,
        null = False,
        blank = False
    )
    textrec = models.TextField(
        verbose_name = 'Текст записи',
        max_length = 1000,
        null = False,
        blank = False
    )
    created_at = models.DateTimeField(
        verbose_name = 'Время создания',
        auto_now_add = True
    )
    changed_at = models.DateTimeField(
        verbose_name = 'Время редактирования',
        auto_now = True
    )
    status = models.CharField(
        verbose_name = 'Статус',
        max_length = 10,
        choices = StatusChoices.choices,
        null = False,
        blank = False,
        default = 'active'
    )

    def __str__(self) -> str:
        return f'{self.author_name}, {self.author_email}, {self.status}'
