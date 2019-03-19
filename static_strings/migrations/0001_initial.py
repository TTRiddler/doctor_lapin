# Generated by Django 2.1.7 on 2019-03-18 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MailFromString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_use_tls', models.BooleanField(default=True, verbose_name='EMAIL_USE_TLS')),
                ('email_port', models.PositiveIntegerField(default=587, verbose_name='EMAIL_PORT')),
                ('email_host', models.CharField(max_length=250, verbose_name='EMAIL_HOST')),
                ('email_host_user', models.EmailField(max_length=250, verbose_name='EMAIL_HOST_USER')),
                ('email_host_password', models.CharField(max_length=250, verbose_name='EMAIL_HOST_PASSWORD')),
            ],
            options={
                'verbose_name': 'Откуда отправлять',
                'verbose_name_plural': 'Откуда отправлять',
            },
        ),
        migrations.CreateModel(
            name='MailToString',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=250, verbose_name='E-mail')),
            ],
            options={
                'verbose_name': 'Кому отправлять',
                'verbose_name_plural': 'Кому отправлять',
            },
        ),
    ]
