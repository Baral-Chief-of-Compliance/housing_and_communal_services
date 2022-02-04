from django.db import models
from datetime import date
from django.urls import reverse
# Create your models here.


class News(models.Model):
    name_of_news = models.CharField("Заголовок Новости", max_length = 200)
    date_of_news = models.DateField("Дата Новости", default = date.today)
    text_of_news = models.TextField("Текст Новости")

    def __str__(self):
        return self.name_of_news

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


class Announcement(models.Model):
    name_of_announcement = models.CharField("Заголовок объявления", max_length = 200)
    image_of_announcement = models.ImageField("Изображение объявления", upload_to = 'HCS_site/')

    def __str__(self):
        return self.name_of_announcement

    class Meta:
        verbose_name = "Объявление"
        verbose_name_plural = "Объявления"


class Complaint(models.Model):
    address_of_complaint = models.CharField("Адресс отправителя заявки/жалобы", max_length=200)
    text_of_complaint = models.TextField("Текст заявки/жалобы")
    date_of_complaint = models.DateField("Дата заявки/жалобы", default = date.today)

    def __str__(self):
        return self.address_of_complaint

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обращения"


class Comments(models.Model):
    news = models.ForeignKey(News, verbose_name = "Новось", on_delete = models.CASCADE )
    date_of_comment = models.DateField("Даты коментария", default = date.today)
    name_of_commenter = models.CharField("Имя автора коменатрия", max_length = 200)
    text_of_comment = models.TextField("Текст коментария", max_length  = 5000)

    def __str__(self):
        return f"{self.name_of_commenter} - {self.news}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
