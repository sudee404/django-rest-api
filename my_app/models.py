from django.db import models

# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Service,null=True,on_delete=models.SET_NULL)
    description = models.TextField()
    source_link = models.URLField()
    web_link = models.URLField(null=True)
    poster = models.ImageField(upload_to='poster')
    
    def __str__(self):
        return self.name