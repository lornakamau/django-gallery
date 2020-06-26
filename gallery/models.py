from django.db import models

# Create your models here.
class Image(models.Model):
    image= models.ImageField(upload_to = 'images/')
    description = models.CharField(max_length = 40)
    name= models.CharField(max_length = 30)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    location = models.ForeignKey(Location, on_delete=models.DO_NOTHING)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
