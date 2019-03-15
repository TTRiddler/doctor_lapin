from django.db import models
from tinymce import HTMLField


class Seminar(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    description = HTMLField(verbose_name='Описание')
    date = models.DateField(verbose_name='Дата проведения')
    city = models.CharField(max_length=250, verbose_name='Город')
    days_number = models.PositiveSmallIntegerField(verbose_name='Количество дней', default=1)
    hours_number = models.PositiveSmallIntegerField(verbose_name='Академических часов', default=1)
    
    class Meta:
        verbose_name = 'Семинар'
        verbose_name_plural = 'Все семинары'
        ordering = ['date']
    
    def seminars_dates(self):
        dates = ''
        date = self.date
        days_number = self.days_number
        return str(days_number)

    def __str__(self):
        return '%s - %s' % (self.title, self.date)
