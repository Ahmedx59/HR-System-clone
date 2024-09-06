from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=12, null = True , blank = True)
    email = models.EmailField(max_length=50, null = True , blank = True)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    branch = models.ForeignKey('Branch', related_name="departmentsBranch", on_delete=models.CASCADE)

    def __str__(self):
        return self.name