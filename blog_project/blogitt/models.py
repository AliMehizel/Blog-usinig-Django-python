from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.

class Post(models.Model):
    auth = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=800)
    image = models.ImageField(null=True, blank=True)
    created_on = models.DateField(default= date.today)
    
    class Meta:
        ordering = ["-created_on"]
        
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    commentText = models.TextField(max_length=800)
    commentDate = models.DateField(default=date.today)
    
    class Meta:
        ordering = ["-commentDate"]
        
    def __str__(self):
        return str(self.id)
 
