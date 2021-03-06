import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    def __str__(self):
        return self.text

    text = models.TextField("soru metni", max_length=300)
    pub_date = models.DateTimeField('ekleme tarihi')
    degree = models.PositiveSmallIntegerField("zorluk derecesi",default=1)
    subject = models.CharField("konu", max_length=30, default="Genel")

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    def __str__(self):
        return self.text
        
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="sahip soru")
    text = models.CharField("seçenek metni", max_length=150)
    votes = models.IntegerField("oy sayısı", default=0)
    correct = models.BooleanField("seçenek doğru mu?",default=False)