from django.contrib import admin
from .models import Produit, Articles, Panier

admin.site.register(Produit)
admin.site.register(Articles)
admin.site.register(Panier)