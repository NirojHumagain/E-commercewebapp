from django.db import models
STATUS = (('active','active'),('','default'))
STATUSS = (('sale','sale'),('hot','hot'),('new','new'),('','default'))
#('for database','we see')
class Item(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discounted_price = models.FloatField(blank = True)
    image = models.TextField()
    description = models.TextField()
    slug = models.CharField(max_length=200)
    brand = models.CharField(max_length=200,blank = True)
    status = models.CharField(max_length=100,choices=STATUSS,blank = True)
    def __str__(self):
        return self.title

class Brand(models.Model):
    name = models.CharField(max_length=200)
    image = models.TextField()
    description = models.TextField()
    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=200)
    image = models.TextField(max_length = 300)
    rank = models.IntegerField()
    add_date = models.DateTimeField(auto_now_add=True)
    status= models.CharField(choices=STATUS,max_length=100,blank = True)
    description = models.TextField()
    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=200)
    image = models.TextField(max_length=300)
    rank = models.IntegerField()
    status = models.CharField(choices=STATUS, max_length=100, blank=True)
    description = models.TextField()
    text_one=models.CharField(max_length=200)
    text_two=models.CharField(max_length=200)
    text_three=models.CharField(max_length=200)
    url = models.TextField()

    def __str__(self):
        return self.name
