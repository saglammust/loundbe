# Generated by Django 3.2.4 on 2021-08-16 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20210816_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='correct',
            field=models.BooleanField(default=False, verbose_name='seçenek doğru mu?'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.question', verbose_name='sahip soru'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='text',
            field=models.CharField(max_length=200, verbose_name='seçenek metni'),
        ),
        migrations.AlterField(
            model_name='choice',
            name='votes',
            field=models.IntegerField(default=0, verbose_name='oy sayısı'),
        ),
        migrations.AlterField(
            model_name='question',
            name='text',
            field=models.CharField(max_length=255, verbose_name='soru metni'),
        ),
    ]
