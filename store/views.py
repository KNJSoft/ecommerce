from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from store.models import Produit, Panier, Articles


def index(request):
    prd=Produit.objects.all()
    return render(request,'store/index.html',{"produits":prd})

def produit_detail(request,slug):
    produit=get_object_or_404(Produit,slug=slug)
    return render(request,'store/slog.html',context={"produit":produit})

def ajouter_au_panier(request,slug):
    user=request.user
    produit=get_object_or_404(Produit,slug=slug)
    panier,_=Panier.objects.get_or_create(user=user)#recupere le panier si'il exite ou le crait sinon # (_) parceque  la fonction retourne  valeurs et on utilise pas la  valeur
    article,created=Articles.objects.get_or_create(user=user,statut=False,produit=produit)
    if created:
        panier.articles.add(article)
        panier.save()
    else:
        article.quantite+=1
        article.save()
    return redirect(reverse("produit",kwargs={"slug":slug}))

def panier(request):
    panier=get_object_or_404(Panier,user=request.user)#on recupere un obj panier s'il exite ou return erreur 404

    return render(request,'store/panier.html',context={'article': panier.articles.all()})

def delete_panier(request):
    panier=request.user.panier
    if panier:
        panier.delete()
    return redirect('index')
"""if panier :=request.user.panier:
        panier.articles.all().delete()"""