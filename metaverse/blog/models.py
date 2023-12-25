from django.db import models

# Create your models here.


class contactFormModel(models.Model):
    username= models.CharField(max_length=50, verbose_name= 'Name Surname')
    message= models.TextField(max_length=250, verbose_name= 'Your Message')
    
    def __str__(self):
        return self.username