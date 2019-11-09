from django.db import models


class Currency(models.Model):
    number = models.IntegerField(verbose_name='ID', null=True)
    date = models.DateField(verbose_name='Date')
    value = models.FloatField(verbose_name='Value')
    price = models.FloatField(verbose_name='Cost in rubles')

    def __str__(self):
        return str(self.number) + ' ' + str(self.date)
