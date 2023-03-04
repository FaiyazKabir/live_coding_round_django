from django.db import models

# Create your models here.
class Playlist(models.Model):
    name = models.CharField(unique=False, max_length=150)
    user = models.ForeignKey("auth.User",null=False,blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" % self.name

class Songs(models.Model):
    name = models.CharField(unique=False,max_length=150)
    author = models.CharField(unique=False,max_length=150)
    playlist = models.ForeignKey(Playlist,null=True,blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s" %self.name