from datetime import date
from django.db import models


class Review(models.Model):
    email = models.EmailField(max_length=250, verbose_name='E-mail')
    name = models.CharField(max_length=250, verbose_name='Имя')
    text = models.TextField(verbose_name='Текст')
    published = models.BooleanField(default=False, verbose_name='Активно')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.email, ext)
        return 'images/reviews/%s' % filename

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Фото', null=True, blank=True)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Все отзывы'
        ordering = ['-created_date']

    def __str__(self):
        return '%s - %s' % (self.id, self.email)