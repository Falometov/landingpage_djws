from django.contrib import admin
from .models import Request, StatusCrm, CommentCrm


class Comment(admin.StackedInline):
    model = CommentCrm
    fields = ('comment_dt', 'comment_text')
    readonly_fields = ('comment_dt',)
    extra = 0

class RequestAdm(admin.ModelAdmin):
    list_display = ('id', 'request_status', 'request_plan', 'request_name', 'request_email', 'request_dt')
    list_display_links = ('id', 'request_name')
    search_fields = ('id', 'request_name', 'request_email')
    list_filter = ('request_status', 'request_plan')
    list_editable = ('request_status',)
    list_per_page = 10
    fields = ('id', 'request_dt', 'request_status', 'request_plan', 'request_name', 'request_email')
    readonly_fields = ('id', 'request_dt')
    inlines = [Comment,]

# Register your models here.
admin.site.register(Request, RequestAdm)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
