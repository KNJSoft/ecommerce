from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone

from shop.settings import AUTH_USER_MODEL

"""""le model produit
-Nom:char
-Prix:float
-stock:int
-description
-image"""

class Produit(models.Model):
    nom=models.CharField(max_length=75)
    slug=models.SlugField(max_length=75)
    prix=models.FloatField(default=0.0)
    stock=models.IntegerField(default=0)
    description=models.TextField(blank=True)
    photo=models.ImageField(upload_to="produit")

    def __str__(self):
        return f"{self.nom}"

    def get_absolute_url(self):
        return reverse("produit",kwargs={"slug":self.slug})


#model articles&order
"""
-user: join()
-produit: join()
-qte :int
-statut: commandé ou non(bool) par défaut False
"""
class Articles(models.Model):
    user=models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)#on supprime tous les elements relier a l'user
    produit=models.ForeignKey(Produit,on_delete=models.CASCADE)
    quantite=models.IntegerField(default=1)
    statut=models.BooleanField(default=False)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.produit.nom}({self.quantite})"

#model panier&cart
""""
-user: 1-1
-articles :n-n
-statut commandé ou non(bool) par défaut False
-Date: date de la commande
"""

class Panier(models.Model):
    user=models.OneToOneField(AUTH_USER_MODEL,on_delete=models.CASCADE)
    articles=models.ManyToManyField(Articles)


    def __str__(self):
        return self.user.username

    def delete(self, *args,**kwargs):
        for article in self.articles.all():
            article.statut=True
            article.date=timezone.now()
            article.save()
        self.articles.clear()
        super().delete(*args,**kwargs)