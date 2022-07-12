"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from shop import settings
from store.views import index, produit_detail, ajouter_au_panier, panier,delete_panier
from compte.views import signup, logout_user, login_user

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/',signup,name="signup"),
    path('logout/',logout_user,name="logout"),
    path('login/',login_user,name="login"),
    path('panier/', panier, name="panier"),
    path('panier/delete', delete_panier, name="delete_panier"),
    path('',index,name="index" ),
    path('produit/<str:slug>/', produit_detail,name="produit"),
    path('produit/<str:slug>/ajouter_au_panier/', ajouter_au_panier,name="ajouter_au_panier"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
