from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=500)


person_CHOICES=(
    ('1','Person1'),
    ('2','Person2'),
    ('3','Person3'),
    ('4','Person4')
)

class BookTable(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    date = models.DateField()
    time = models.TimeField()
    person = models.CharField(max_length=90,choices=person_CHOICES)   