from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User # importing User table from admin

# each model will be its own table in the database
class Post(models.Model):    # inherits from django.db.models
    title= models.CharField(max_length=100)
    content=models.TextField()
    date_posted = models.DateTimeField(default=timezone.now) # we only want to pass the function closure to default, not timezone.now() or it would evaluate the function once and keep that value
    author = models.ForeignKey(User, on_delete=models.CASCADE) # on_delete means if User is deleted, then what happens --> well for models.CASCADE means that everything they did is deleted too

    def __str__(self):
        return self.title
