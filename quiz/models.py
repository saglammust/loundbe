from django.db import models

class Question(models.Model):
    def __str__(self):
        return self.soru

    soru = models.fields.CharField(max_length=255) #* soru yazısı
    tarih = models.fields.DateTimeField('yayım tarihi')
    zorluk = models.fields.SmallIntegerField(default=1)

class Choice(models.Model):
    def __str__(self):
        return self.cevap
    
    soru = models.ForeignKey(Question, on_delete=models.CASCADE)
    cevap = models.fields.CharField(max_length=127)
    oylar = models.fields.IntegerField(default=0)
    dogru = models.fields.BooleanField(default=False)
