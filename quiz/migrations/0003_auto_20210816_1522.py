# Generated by Django 3.2.4 on 2021-08-16 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_auto_20210816_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='degree',
            field=models.PositiveSmallIntegerField(default=1, verbose_name='zorluk derecesi'),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='ekleme tarihi'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=255, verbose_name='soru'),
        ),
    ]
