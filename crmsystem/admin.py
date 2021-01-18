from django.contrib import admin
from .models import Request, StatusCrm, CommentCrm

# Register your models here.
admin.site.register(Request)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)
