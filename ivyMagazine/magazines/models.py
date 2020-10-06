from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null =True)
    email = models.CharField(max_length=200, null =True)
    data_created = models.DateTimeField(auto_now_add=True, null =True)

    def __str__(self):
        return self.name

class Magazine(models.Model):
    CATEGORY = (
        ('Spring2019', 'Spring2019'),
        ('Fall2019', 'Fall2019'),
        ('Spring2020', 'Spring2020')
    )

    name = models.CharField(max_length=200, null =True)
    price = models.FloatField(null = True)
    category = models.CharField(max_length=200, null =True, choices=CATEGORY)
    description = models.CharField(max_length=300, null =True) #blank=True
    pdf = models.FileField(null =True, blank = True)

    def save(self, *args, **kwargs):
        super(Magazine, self).save(*args, **kwargs)
        filename = self.pdf.url

    def __str__(self):
        return self.name
    
class Portfolio(models.Model):

    name = models.CharField(max_length=200, null =True)
    caption = models.CharField(max_length=100, null =True) #blank=True
    date_created = models.DateTimeField(auto_now_add=True, null =True)
    images = models.FileField(null =True, blank = True)

    def save(self, *args, **kwargs):
        super(Portfolio, self).save(*args, **kwargs)
        filename = self.images.url

    def __str__(self):
        return self.name

