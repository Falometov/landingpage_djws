from django.contrib import admin
from .models import Request, StatusCrm, CommentCrm

# Register your models here.
admin.site.register(Request)
admin.site.register(StatusCrm)
admin.site.register(CommentCrm)

# https://api.telegram.org/bot1548163787:AAHIM7Wm5_ekv9TM3EdYGqiOlysB5oD-Wvw/sendMessage?chat_id=-444411535&text=testmessage