from django.db import models

class Email(models.Model):
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.value
 
class Host(models.Model):
    value = models.CharField(max_length=253) 

    def __str__(self):
        return self.value