from django.db import models
# Create your models here.
from django.contrib.auth.models import User
m = User.objects.filter(username='marcel')[0]


class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    photo = models.ImageField(upload_to='testons', default='a.jpg')

    def __str__(self):
        return self.titre

    def __unicode__(self):
        return self.titre
