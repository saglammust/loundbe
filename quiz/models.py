import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    def __str__(self):
        return self.text

    text = models.CharField("soru metni", max_length=255)
    pub_date = models.DateTimeField('ekleme tarihi')
    degree = models.PositiveSmallIntegerField("zorluk derecesi",default=1)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Tag(models.Model):
    def __str__(self):
        return self.text

    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="sahip soru")
    text = models.CharField("konu", max_length=30)

class Choice(models.Model):
    def __str__(self):
        return self.text
        
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="sahip soru")
    text = models.CharField("seçenek metni", max_length=200)
    votes = models.IntegerField("oy sayısı", default=0)
    correct = models.BooleanField("seçenek doğru mu?",default=False)