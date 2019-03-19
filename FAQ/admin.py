from django.contrib import admin
from .models import Qna

class FAQAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register( Qna, FAQAdmin)
