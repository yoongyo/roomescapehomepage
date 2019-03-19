from django.contrib import admin
from .models import Bulletinboard, Comment


class BulletinboardAdmin(admin.ModelAdmin):
    list_display = ['title', 'writer']

class CommentAdmin(admin.ModelAdmin):
    list_display = ['writer', 'text']
    
admin.site.register(Bulletinboard, BulletinboardAdmin)
admin.site.register(Comment, CommentAdmin)
