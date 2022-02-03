from django.db import models
from datetime import date
from django.urls import reverse
# Create your models here.


class News(models.Model):
    name_of_news = models.CharField("Заголовок Новости", max_length=200)
    date_of_news = models.DateField("Дата Новости", default = date.today)
    text_of_news = models.TextField("Текст Новости")


class Announcement(models.Model):
    name_of_announcement = models.CharField("Заголовок объявления", max_length=200)
    image_of_announcement = models.ImageField("Изображение объявления", upload_to = 'HCS_site/')


class Complaint(models.Model):
    address_of_complaint = models.CharField("Адресс отправителя заявки/жалобы", max_length=200)
    text_of_complaint = models.TextField("Текст заявки/жалобы")
    date_of_complaint = models.DateField("Дата заявки/жалобы", default = date.today)


class Comments(models.Model):
    date_of_comment = models.DateField("Даты коментария", default = date.today)
    name_of_commenter = models.CharField("Имя автора коменатрия", max_length=200)
    text_of_comment = models.TextField("Текст коментария")
