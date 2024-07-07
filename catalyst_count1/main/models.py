from django.db import models

# Create your models here.

# Create your models her
# thik     wo apne pura migrate kiya hai naa to jitna v packages wala but ye sab hai kaha unka khudka app rhega ushme hoga sya
class Company(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    city = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    email = models.EmailField()

class Companydata(models.Model):
    com=models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255)
    year_founded = models.IntegerField(default=0)
    industry = models.CharField(max_length=255)
    locality = models.TextField()
    country = models.CharField(max_length=255)
    linkedin_url = models.URLField(max_length=255, blank=True, null=True)  # URLField for URLs
    current_employee_estimate = models.IntegerField(default=0)	
    total_employee_estimate =models.IntegerField(default=0)

    def __str__(self):
        return self.name 

