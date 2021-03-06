# Generated by Django 3.2.3 on 2022-02-04 11:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_announcement', models.CharField(max_length=200, verbose_name='Заголовок объявления')),
                ('image_of_announcement', models.ImageField(upload_to='HCS_site/', verbose_name='Изображение объявления')),
            ],
            options={
                'verbose_name': 'Объявление',
                'verbose_name_plural': 'Объявления',
            },
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_of_complaint', models.CharField(max_length=200, verbose_name='Адресс отправителя заявки/жалобы')),
                ('text_of_complaint', models.TextField(verbose_name='Текст заявки/жалобы')),
                ('date_of_complaint', models.DateField(default=datetime.date.today, verbose_name='Дата заявки/жалобы')),
            ],
            options={
                'verbose_name': 'Обращение',
                'verbose_name_plural': 'Обращения',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_news', models.CharField(max_length=200, verbose_name='Заголовок Новости')),
                ('date_of_news', models.DateField(default=datetime.date.today, verbose_name='Дата Новости')),
                ('text_of_news', models.TextField(verbose_name='Текст Новости')),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_comment', models.DateField(default=datetime.date.today, verbose_name='Даты коментария')),
                ('name_of_commenter', models.CharField(max_length=200, verbose_name='Имя автора коменатрия')),
                ('text_of_comment', models.TextField(max_length=5000, verbose_name='Текст коментария')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HCS_site.news', verbose_name='Новось')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
