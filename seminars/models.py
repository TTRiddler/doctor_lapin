from datetime import datetime
from django.db import models
from django.urls import reverse
from tinymce import HTMLField


class Seminar(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    description = HTMLField(verbose_name='Описание')
    days_number = models.PositiveSmallIntegerField(verbose_name='Количество дней', default=1)
    hours_number = models.PositiveSmallIntegerField(verbose_name='Академических часов', default=1)
    in_index = models.BooleanField(default=False, verbose_name='Отображать на главной', help_text='Отображаюся только 6 выбранных семинаров')
    video = models.CharField(max_length=250, verbose_name='Ссылка на видео', blank=True, null=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False, verbose_name='Сортировка')

    def get_picture_url(self, filename):
        ext = filename.split('.')[-1]
        filename = '%s.%s' % (self.id, ext)
        year = datetime.now().year
        month = datetime.now().month
        return 'images/seminars/%s.%s/%s' % (month, year, filename)
    
    def get_absolute_url(self):
        return reverse('seminar_detail', args=[self.id])

    image = models.ImageField(upload_to=get_picture_url, verbose_name='Изображение')
    
    class Meta:
        verbose_name = 'Семинар'
        verbose_name_plural = 'Все семинары'
        ordering = ['my_order']

    def __str__(self):
        return '%s' % self.title


class UpcomingSeminar(models.Model):
    seminar = models.ForeignKey(Seminar, on_delete=models.CASCADE, verbose_name='Заголовок', related_name='upcoming_seminars')
    date_start = models.DateField(verbose_name='Дата начала')
    date_end = models.DateField(verbose_name='Дата завершения')
    city = models.CharField(max_length=250, verbose_name='Город')
    
    class Meta:
        verbose_name = 'Ближайший семинар'
        verbose_name_plural = 'Ближайшие семинары'
        ordering = ['date_start']

    def __str__(self):
        return '%s: %s-%s' % (self.seminar, self.date_start, self.date_end)
