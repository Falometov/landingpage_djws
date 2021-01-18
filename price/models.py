from django.db import models

# Create your models here.
class PriceCard(models.Model):
    pc_name = models.CharField(max_length=50, verbose_name='Name')
    pc_value = models.FloatField(max_length=10, verbose_name='Value')


    def __str__(self):
        return self.pc_name

    class Meta:
        verbose_name = 'Card'
        verbose_name_plural = 'Cards'