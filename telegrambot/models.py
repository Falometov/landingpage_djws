from django.db import models

# Create your models here.
class TgSettings(models.Model):
    tg_token = models.CharField(max_length=200, verbose_name='Token')
    tg_chat_id = models.CharField(max_length=200, verbose_name='Chat ID')
    tg_text = models.TextField(verbose_name='Text')

    def __str__(self):
        return self.tg_chat_id

    class Meta:
        verbose_name = 'Setting'
        verbose_name_plural = 'Settings'
