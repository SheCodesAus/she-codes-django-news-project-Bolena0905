from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass
    def __str__(self):
        return self.username

# class Product(models.Model):
#     title = models.CharField(max_length=200)
#     favourite = models.ManyToManyField(User, related_name='user_favourite')