from django.contrib import admin
from models import User, Fileserver, name_password
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')
    search_fields = ('username', 'email')

class userageAdmin(admin.ModelAdmin):
    list_display = ('disk_useage', 'smb_status', 'raid_status')
class serverAdmin(admin.ModelAdmin):
    list_display = ('IP', 'username', 'password')
admin.site.register(User, AuthorAdmin)
admin.site.register(Fileserver, userageAdmin)
admin.site.register(name_password, serverAdmin)
# Register your models here.
