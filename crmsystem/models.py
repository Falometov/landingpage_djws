from django.db import models

# Create your models here.
class Order(models.Model):
    order_dt = models.DateTimeField(auto_now=True)
    order_name = models.CharField(max_length=200, verbose_name='Name')
    order_email = models.EmailField(max_length=200, verbose_name='Email')
    order_plan = models.CharField(max_length=200, verbose_name='Plan')


class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Status name')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Statuses'


class Request(models.Model):
    request_dt = models.DateTimeField(auto_now=True, verbose_name='Data')
    request_name = models.CharField(max_length=200, verbose_name='Name')
    request_email = models.EmailField(max_length=200, verbose_name='Email')
    request_plan = models.CharField(max_length=200, verbose_name='Plan')
    request_status = models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Status')

    def __str__(self):
        return self.request_email

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'


class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Request, on_delete=models.CASCADE, verbose_name='Request')
    comment_text = models.TextField(verbose_name='Comment')
    comment_dt = models.DateTimeField(auto_now=True, verbose_name='Data')

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
