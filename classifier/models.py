from django.db import models

# Create your models here.

class Imgpath(models.Model):
    image = models.ImageField(("Image"), upload_to="images/")
    imgpath = models.TextField(("Image path"))

    def __str__(self):
        return self.imgpath

