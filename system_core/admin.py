from django.contrib import admin
from .models import Autor,Video,Tag,Khatira,Sound,Mail,Sidebar

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'autor', 'date_creation','views')
    list_filter = ("date_creation","autor")
    search_fields = ['title','description']

class AutorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'username', 'email','birthday')
    list_filter = ("birthday","email")
    search_fields = ['full_name','username','email']

class KhatiraAdmin(admin.ModelAdmin):
    list_display = ('title', 'autor', 'date_creation','views')
    list_filter = ("date_creation","autor")
    search_fields = ['title','text']

class SoundAdmin(admin.ModelAdmin):
    list_display = ('title', 'autor', 'date_creation','views')
    list_filter = ("date_creation","autor")
    search_fields = ['title','description']

class MailAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'subject','email_sender', 'date_creation')
    list_filter = ("date_creation","email_sender")
    search_fields = ['subject','full_name','text','email_sender']

class SidebarAdmin(admin.ModelAdmin):
    list_display = ('title', 'HTML',)
    
    
admin.site.register(Video, VideoAdmin)

admin.site.register(Autor, AutorAdmin)
admin.site.register(Sidebar,SidebarAdmin)
admin.site.register(Tag)
admin.site.register(Khatira, KhatiraAdmin)
admin.site.register(Sound, SoundAdmin)
admin.site.register(Mail, MailAdmin)