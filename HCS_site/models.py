from django.db import models
# Create your models here.


class News(models.Model):
    name_of_news = models.CharField(max_length=200)
    
