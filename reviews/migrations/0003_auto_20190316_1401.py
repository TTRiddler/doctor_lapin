# Generated by Django 2.1.7 on 2019-03-16 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20190316_1400'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ['-created_date'], 'verbose_name': 'Отзыв', 'verbose_name_plural': 'Все отзывы'},
        ),
    ]