from django.db import models

# Create your models here.

class admindata(models.Model):
    name = models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    contact=models.CharField(max_length=100)
    email=models. CharField (max_length=100,primary_key=True)
    def __str__(self): #python 2 def __unicode__(self):
        return self.email

class logindata(models.Model):
    email=models. CharField (max_length=100,primary_key=True)
    password=models.CharField(max_length=100)
    usertype=models.CharField(max_length=100)
    def __str__(self):
        return self.email

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
