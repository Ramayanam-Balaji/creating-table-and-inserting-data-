from django.db import models

# Create your models here.
class Country(models.Model):
    cname=models.CharField(max_length=100,primary_key=True)
    cid=models.IntegerField()
    def __str__(self) -> str:
        return self.cname
class Capital(models.Model):
    cid=models.ForeignKey(Country,on_delete=models.CASCADE)
    capital_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self) -> str:
        return self.capital_name
    
