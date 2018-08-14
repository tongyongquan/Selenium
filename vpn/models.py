from django.db import models
import datetime
# Create your models here.


class VpnInfo(models.Model):

    email = models.CharField(max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True,default=datetime.datetime.now())
    total = models.CharField(max_length=20, blank=True, null=True)
    used = models.CharField(max_length=20, blank=True, null=True)
    un_used = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    port = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    encryption = models.CharField(max_length=20, blank=True, null=True)
    last_login = models.CharField(max_length=20, blank=True, null=True)
    last_check_in = models.CharField(max_length=20, blank=True, null=True)