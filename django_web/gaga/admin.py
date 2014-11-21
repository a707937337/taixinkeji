from django.contrib import admin
from models import User, Fileserver
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')
    search_fields = ('username', 'email')

class userageAdmin(admin.ModelAdmin):
    list_display = ('disk_useage', 'smb_status', 'raid_status')
admin.site.register(User, AuthorAdmin)
admin.site.register(Fileserver, userageAdmin)
# Register your models here.
