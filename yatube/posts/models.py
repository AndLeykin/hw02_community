from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='название')
    slug = models.SlugField(unique=True, verbose_name='уникальный адрес')
    description = models.TextField(default='',
                                   verbose_name='описание сообщества')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщество'
        verbose_name_plural = 'cообщества'


class Post(models.Model):
    text = models.TextField(verbose_name='текст')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='дата публикации')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='пользователь'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name='сообщество'
    )

    def __str__(self):
        post_description = (f'публикация пользователя {self.author} от '
                            f'{self.pub_date.strftime("%d.%m.%Y, %H:%M:%S")}: '
                            f'{self.text[:50]}...'
                            )
        return post_description

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'публикации'
        ordering = ['-pub_date']
