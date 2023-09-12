from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение', )
    # scope = models.ManyToManyField('Tag', through='Scope', through_fields=('article', 'tag'),
    #                                   verbose_name='Темы')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Tag(models.Model):

    tag_name = models.CharField(max_length=60, unique=True, verbose_name='Темы')
    articles = models.ManyToManyField(Article, related_name='scopes', through='Scope')

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['-tag_name']

    def __str__(self):
        return self.tag_name


class Scope(models.Model):

    article = models.ForeignKey('Article', on_delete=models.CASCADE,  verbose_name='Статья')
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE, related_name='scopes', verbose_name='Тема')
    is_main = models.BooleanField(default=False, verbose_name='Основная тематика')

    class Meta:
        verbose_name = 'Тематика статьи'
        verbose_name_plural = 'Тематики статей'