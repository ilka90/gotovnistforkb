from django.db import models

class Articles(models.Model):
    #title, anons, full_text, date
    title = models.CharField('Навза новини', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Новина')
    date = models.DateTimeField('Дата публікації')

    class Meta:
        verbose_name = 'Новина'
        verbose_name_plural = 'Новини'

    