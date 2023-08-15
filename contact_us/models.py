from django.db import models

# Create your models here.
class Footer(models.Model):
    address=models.CharField(max_length=250)
    email=models.EmailField()
    city=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    whatsapp=models.CharField(max_length=100)
    telegrem=models.CharField(max_length=100)
    instagram=models.CharField(max_length=100)

class Message(models.Model):
    fname=models.CharField(max_length=50)
    sub=models.CharField(max_length=50)
    email=models.EmailField()
    body=models.TextField()

    def __str__(self):
        return f' {self.fname}-{self.email}'