# Generated by Django 2.1.7 on 2019-03-21 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seminars', '0006_seminar_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seminar',
            name='video',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name='Ссылка на видео'),
        ),
    ]
