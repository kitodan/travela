from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# imports
from safedelete.models import SafeDeleteModel
from safedelete.models import HARD_DELETE_NOCASCADE

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='download.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'



    def save(self):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 100 or img.width > 100:
            output_size = (100,100)
            img.thumbnail(output_size)
            img.save(self.image.path)




# Models
class Article(SafeDeleteModel):
    safedelete_policy = HARD_DELETE_NOCASCADE
    name = models.CharField(max_length=100)

class Order(SafeDeleteModel):
    safedelete_policy = HARD_DELETE_NOCASCADE
    name = models.CharField(max_length=100)
    articles = models.ManyToManyField(Article)
