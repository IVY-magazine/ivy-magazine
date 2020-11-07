from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200, null =True)

    def __str__(self):
        return self.name    

class Customer(models.Model):
    name = models.CharField(max_length=200, null =True)
    email = models.CharField(max_length=200, null =True)
    data_created = models.DateTimeField(auto_now_add=True, null =True)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name

 

class Magazine(models.Model):
   

    name = models.CharField(max_length=200, null =True)
    price = models.FloatField(null = True)
    # category = models.CharField(max_length=200, null =True, choices=CATEGORY)
    description = models.CharField(max_length=300, null =True) 
    description2 = models.CharField(max_length=300, null =True)#blank=True
    pdf = models.FileField(null =True, blank = True)
    thumbNail = models.FileField(null = True, blank = True)
    date_created = models.DateTimeField(auto_now_add=True, null =True)

    def save(self, *args, **kwargs):
        super(Magazine, self).save(*args, **kwargs)
        filename = self.pdf.url
        thumbNailLink = self.thumbNail.url

    def __str__(self):
        return self.name
    
# class Portfolio(models.Model):

#     name = models.CharField(max_length=200, null =True)
#     caption = models.CharField(max_length=100, null =True) #blank=True
#     date_created = models.DateTimeField(auto_now_add=True, null =True)
#     images = models.FileField(null =True, blank = True)

#     def save(self, *args, **kwargs):
#         super(Portfolio, self).save(*args, **kwargs)
#         filename = self.images.url

#     def __str__(self):
#         return self.name

from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    involvedEditor = models.TextField(blank=True)
    image = models.FileField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null =True)
    viewcount = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title
    
    @property
    def update_viewcount(self):
        self.viewcount = self.viewcount + 1
        self.save()
        return self.viewcount

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'static/images/posts')

    def __str__(self):
        return self.post.title
