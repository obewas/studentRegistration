from django.db import models

# Create your models here.
class Student(models.Model):

  firstName = models.CharField(max_length=100)
  lastName = models.CharField(max_length=100)
  email = models.EmailField()
  dateOfBirth = models.DateField(auto_now_add=False)
  course = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.firstName + " " + self.lastName
  

  
