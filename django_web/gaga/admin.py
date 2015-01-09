from django.contrib import admin
from models import User, Fileserver, name_password, linux_server
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')
    search_fields = ('username', 'email')

class userageAdmin(admin.ModelAdmin):
    list_display = ('disk_useage', 'smb_status', 'raid_status')
class serverAdmin(admin.ModelAdmin):
    list_display = ('IP', 'username', 'password')
class linux_ssh(admin.ModelAdmin):
    list_display = ('serverip', 'mingcheng', 'leixing', 'version')
admin.site.register(User, AuthorAdmin)
admin.site.register(Fileserver, userageAdmin)
admin.site.register(name_password, serverAdmin)
admin.site.register(linux_server, linux_ssh)
# Register your models here.
