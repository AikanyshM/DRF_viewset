from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=50)
    office_address = models.CharField(max_length=50)

    def __str__(self):
        return self.company_name

class Category(models.Model):
    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name

class Inventory(models.Model):
    name = models.CharField(max_length=20)
    cost = models.FloatField()
    amount = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name