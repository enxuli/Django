from django.db import models
from django.utils.text import slugify

# Create your models here.
class Plan(models.Model):
    name = models.CharField(max_length = 100)
    slug = models.SlugField(max_length = 100, unique = True, blank =True)
    budget = models.DecimalField(max_digits=10,decimal_places=2)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Plan,self).save(*args, **kwargs)

class Category(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)

class Expense(models.Model):
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE,related_name="expenses")
    title = models.CharField(max_length = 100)
    amount = models.DecimalField(max_digits=10,decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
