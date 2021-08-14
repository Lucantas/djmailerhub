from django.db import models
from django import forms
from django.contrib.auth.hashers import make_password

from .utils import Host, Email

from ..utils import *        

class MailConf(models.Model): 
    name = models.CharField(max_length=255, default='')
    description = models.TextField(null=True)
    host = models.CharField(max_length=253) 
    port = models.CharField(max_length=20)
    sender = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    reply_to = models.CharField(max_length=255)
    receivers = models.ManyToManyField(Email, related_name='mail_receivers')
    copies = models.ManyToManyField(Email, related_name='copy_receivers', blank=True)
    plain_password = models.BooleanField()
    use_ssl = models.BooleanField()
    purge_date = models.DateTimeField(null=True, blank=True)
    body = models.TextField()    
    allowed_hosts = models.ManyToManyField(Host, related_name='allowed_hosts')
    subject = models.CharField(max_length=998)

    class Meta:
        verbose_name = 'mail configuration'
        verbose_name_plural = 'mail configurations'

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.name, self.host, self.login)

    def receivers_list(self):
        new_list = []
        for receiver in self.receivers.all():
            new_list.append(receiver.value)
        
        return new_list
    
    def copies_list(self):
        new_list = []
        for copy in self.copies.all():
            new_list.append(copy.value)

        return new_list

    def valid_host(self, host):
        return len(self.allowed_hosts.filter(value=host) ) > 0
