# Generated by Django 2.1.7 on 2019-03-17 08:06

from django.db import migrations, models
import static_elements.models


class Migration(migrations.Migration):

    dependencies = [
        ('static_elements', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SomeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Текст')),
                ('image', models.ImageField(upload_to=static_elements.models.SomeInfo.get_picture_url, verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Инфорамация',
                'verbose_name_plural': 'Информация на главной странице',
            },
        ),
    ]
