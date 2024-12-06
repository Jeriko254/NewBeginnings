from django.db import models

# Create your models here.
class Registration(models.Model):
          fullname = models.CharField(max_length=50)
          username = models.CharField(max_length=50)
          email = models.EmailField()
          password = models.CharField(max_length=50)


          def __str__(self):
               return self.fullname



class ImageModel(models.Model):
    name = models.CharField(max_length=400)
    message = models.CharField(max_length=400)

    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.name