from django.db import models



class ShoeBrand(models.Model):
    modelname = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    

    def __str__(self):
        return f"{self.modelname}"
    
class Member(models.Model):
    shoe = models.ForeignKey(ShoeBrand, on_delete=models.CASCADE, null=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)
    

    def __str__(self):
        return f"{self.firstname} {self.lastname}"