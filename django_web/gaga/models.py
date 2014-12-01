#-*- coding: utf-8 -*-
from django.db import models
# Create your models here.
class User(models.Model):
    username = models.CharField('用户名',max_length = 20)
    password = models.CharField('密码',max_length = 20)
    realname = models.CharField('真实姓名',max_length = 255)
    sex = models.CharField('性别',max_length = 10)
    email = models.EmailField('电子邮箱',blank = True)
    def __unicode__(self):
        return self.username
class Fileserver(models.Model):
    disk_useage = models.CharField('磁盘使用率',max_length = 10)
    smb_status = models.CharField('Samba状态',max_length = 50)
    raid_status = models.CharField('Raid状态',max_length = 50)


    def __unicode__(self):
        return self.disk_useage
    def toJSON(self):
        fields = []
        for field in self._meta.fields:
            fields.append(field.name)
        d = {}
        for attr in fields:
            d[attr] = getattr(self, attr)
        import json
        return json.dumps(d)