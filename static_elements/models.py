from django.db import models
from tinymce import HTMLField


class Quote(models.Model):
    text = models.TextField(verbose_name='Цитата')
    author = models.CharField(max_length=250, verbose_name='Автор')

    class Meta:
        verbose_name = 'Цитата'
        verbose_name_plural = 'Цитата на главной странице'

    def __str__(self):
        return '%s' % self.author


class SomeInfo(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    text = HTMLField(verbose_name='Текст')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.title, ext)
        return 'images/staic_elements/%s' % filename

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Инфорамация'
        verbose_name_plural = 'Информация на главной странице'

    def __str__(self):
        return '%s' % self.title