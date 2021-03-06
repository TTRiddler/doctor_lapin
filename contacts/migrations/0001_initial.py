# Generated by Django 2.1.7 on 2019-03-14 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=250, null=True, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Заголовок')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=250, null=True, verbose_name='E-mail')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emails', to='contacts.Contact', verbose_name='Контакт')),
            ],
            options={
                'verbose_name': 'E-mail',
                'verbose_name_plural': 'E-mail',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='Телефон')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='contacts.Contact', verbose_name='Контакт')),
            ],
            options={
                'verbose_name': 'Телефон',
                'verbose_name_plural': 'Телефоны',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('days_point', models.CharField(max_length=250, null=True, verbose_name='Дни недели')),
                ('time_point', models.CharField(max_length=250, null=True, verbose_name='Время работы')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='contacts.Contact', verbose_name='Контакт')),
            ],
            options={
                'verbose_name': 'Пункт',
                'verbose_name_plural': 'Режим работы',
            },
        ),
        migrations.AddField(
            model_name='address',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to='contacts.Contact', verbose_name='Контакт'),
        ),
    ]
