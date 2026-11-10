from django.db import models

# Create your models here.
class student(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    middlename=models.CharField(max_length=50)
    age=models.IntegerField()
    address=models.CharField(max_length=200)

    def __str__(self):
        return  f'{self.firstname},{self.lastname},{self.middlename},{self.age},{self.address}'
class student1(models.Model):
        student_name=models.CharField(max_length=100)
        email=models.EmailField(max_length=254)
        age=models.IntegerField()
        gender=models.CharField(max_length=10)
        course=models.CharField(max_length=100)
        def __str__ (self):
            return f'{self.student_name},{self.email},{self.age},{self.gender},{self.course}'
         