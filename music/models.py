from django.db import models

# Create your models here.d

class Songs(models.Model):
    title = models.CharField(max_length=225, null=False)
    author = models.CharField(max_length=225, null=False)


    def __str__(self):
        return "{} - {}".format(self.title, self.author)

