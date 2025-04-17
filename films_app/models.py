from django.db import models

# Create your models here.
class Film(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    image = models.ImageField(upload_to = 'images')
    favourite = models.BooleanField(default = False)
    genre = models.CharField(max_length=50, default= False)
    country = models.CharField(max_length=50, default=False)
    
    
    def __str__(self):
        return f'{self.name}    {self.description}   {self.genre}  {self.country}'