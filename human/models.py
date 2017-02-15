from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.CharField(max_length=20,primary_key=True)
    first_name= models.CharField(max_length=200)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    salary = models.IntegerField(default=2000)
    phone_number = models.CharField(max_length=40)

    def __unicode__(self):
        return str(self.emp_id)

class Jobs(models.Model):
    min_salary = models.CharField(max_length=100)
    max_salary = models.CharField(max_length=100)
    job_title = models.CharField(max_length=35)
    employ_id = models.ForeignKey('Employee')
    
    def __unicode__(self):
        return str(self.job_title)

class Department(models.Model):
    dept_name =  models.CharField(max_length=20)
    dept_id = models.CharField(max_length=30,primary_key=True)
    employ_id = models.ForeignKey('Employee')
    
    def __unicode__(self):
        return str(self.dept_id)

    
class Organization(models.Model):
    organization_name = models.CharField(max_length=30,primary_key=True)
    organization_id = models.CharField(max_length=30)
    

    def __unicode__(self):
        return str(self.organization_name)

class Location(models.Model):
    city = models.CharField(max_length=300,primary_key=True)
    state = models.CharField(max_length=200)
    location_id = models.ForeignKey('Organization')#on_delete=models.CASCADE)

    def __unicode__(self):
        return str(self.city)

