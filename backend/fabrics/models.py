from django.db import models

# Create your models here.


class Fabric(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FabricImages(models.Model):
    fabric = models.ForeignKey(Fabric, on_delete=models.CASCADE)
    image = models.FileField(upload_to='fabrics/')

    def __str__(self):
        return self.fabric.name
