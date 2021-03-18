from django.db import models



# Create your models here.
class post(models.Model):

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='photos')
    image2 = models.ImageField(upload_to='photos',blank=True)
    image3 = models.ImageField(upload_to='photos',blank=True)
    Discount = models.CharField(max_length=100,blank=True,help_text="-20% discount")
    description = models.TextField()

    def __str__(self):

        return self.title
