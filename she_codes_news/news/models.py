
from django.contrib.auth import get_user_model
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    def __str__(self):
        return self.name
        
class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image = models.URLField(blank=True, null=True)

    # class Meta:
    #     ordering = ('-pub_date',)


    
