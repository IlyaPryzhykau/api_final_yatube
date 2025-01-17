from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models


MAX_TEXT_LENGTH = 50


User = get_user_model()


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор'
    )

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'Подписки'
        unique_together = ('user', 'following')

    def __str__(self):
        return f'{self.user} -> {self.following}'

    def clean(self):
        if self.user == self.following:
            raise ValidationError("Нельзя подписаться на самого себя.")
        if Follow.objects.filter(
                user=self.user,
                following=self.following).exists():
            raise ValidationError("Такая подписка уже существует.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Group(models.Model):
    title = models.CharField('Имя группы', max_length=200)
    slug = models.SlugField('Идентификатор', unique=True)
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField('Текст поста')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    image = models.ImageField(
        'Изображение',
        upload_to='posts/',
        blank=True
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        verbose_name='Группа',
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        default_related_name = 'posts'

    def __str__(self):
        return (self.text[:MAX_TEXT_LENGTH]
                + ('...' if len(self.text) > MAX_TEXT_LENGTH else ''))


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Публикация'
    )
    text = models.TextField('Текст комментария')
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return (self.text[:MAX_TEXT_LENGTH]
                + ('...' if len(self.text) > MAX_TEXT_LENGTH else ''))
