from django.db import models
from .utils import login_check_in
import datetime
# Create your models here.


class VpnInfo(models.Model):

    email = models.CharField(unique=True, max_length=45, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True, default=datetime.datetime.now())
    total = models.CharField(max_length=20, blank=True, null=True)
    used = models.CharField(max_length=20, blank=True, null=True)
    un_used = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    port = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=20, blank=True, null=True)
    encryption = models.CharField(max_length=20, blank=True, null=True)
    last_login = models.CharField(max_length=20, blank=True, null=True)
    last_check_in = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email

    def check_in(self):
        if self.last_check_in is None or self.last_check_in < datetime.datetime.now():
            vpn = login_check_in(self.email)
            self.total = vpn['total']
            self.used = vpn['used']
            self.un_used = vpn['un_used']
            self.status = vpn['status']
            self.port = vpn['port']
            self.password = vpn['password']
            self.encryption = vpn['encryption']
            self.last_login = vpn['last_login']
            self.last_check_in = vpn['last_check_in']
            self.save()

