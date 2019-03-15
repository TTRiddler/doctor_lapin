from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=250, verbose_name='Заголовок')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return '%s' % self.name


class Address(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='Контакт', related_name='addresses')
    address = models.CharField(max_length=250, verbose_name='Адрес', null=True)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return '%s' % self.address


class Phone(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='Контакт', related_name='phones')
    phone = models.CharField(max_length=20, verbose_name='Телефон', null=True)

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'

    def __str__(self):
        return '%s' % self.phone


class Email(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='Контакт', related_name='emails')
    email = models.CharField(max_length=250, verbose_name='E-mail', null=True)

    class Meta:
        verbose_name = 'E-mail'
        verbose_name_plural = 'E-mail'

    def __str__(self):
        return '%s' % self.email


class Schedule(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name='Контакт', related_name='schedules')
    days_point = models.CharField(max_length=250, verbose_name='Дни недели', null=True)
    time_point = models.CharField(max_length=250, verbose_name='Время работы', null=True)

    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Режим работы'

    def __str__(self):
        return '%s %s' % (self.days_point, self.time_point)
