from django.db import models


# Create your models here.

class Drug(models.Model):

    title = models.CharField(max_length=50)

    stock = models.CharField(max_length=50)
    quantity = models.CharField(max_length=50)
    price = models.CharField(max_length=50)
    
    created_date = models.DateTimeField(auto_now_add=True)
    drug_image = models.FileField(blank = True,null = True,verbose_name="Add Picture")
    def __str__(self):
        return self.title



