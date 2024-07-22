from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class Customer(models.Model):
#     username = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200)

#     def __str__(self):
#          return self.name

class Person(models.Model):
    person = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=50 ,null=True)
    level = models.CharField(max_length=50)
    phone = models.CharField(max_length=20, null=True)
    email = models.CharField(max_length=150, null=True)
    website = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="media/",null=True, blank=True)

    def __str__(self):  
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    


class Education(models.Model):
    person = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    # customer = models.ForeignKey(Customer, null=True, blank=True, on_delete=models.CASCADE)
    year = models.CharField(max_length=100)
    qualification = models.TextField(max_length=250)
    universityname = models.CharField(max_length=100)

    def  __str__(self):
        return self.year
    
class Language(models.Model):
    language = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=7, decimal_places=0, null=True)

    def __str__(self):
        return self.language
    

class Profile(models.Model):
    about = models.CharField(max_length=255)

    def __str__(self):
        return self.about
    
class Experience(models.Model):
    year_company = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    about_job = models.TextField(max_length=255)

    def __str__(self):
        return self.year_company
    

class Skills(models.Model):
    skill = models.CharField(max_length=30)
    value = models.DecimalField(max_digits=7, decimal_places=0, null=True)

    def __str__(self):
        return self.skill
    

class Interest(models.Model):
    interests = models.CharField(max_length=20)
        
    def __str__(self):
        return self.interests
