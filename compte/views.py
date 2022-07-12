from django.contrib.auth import get_user_model, login, logout,authenticate
from django.shortcuts import render, redirect

User=get_user_model()
def signup(request):
    if request.method=="POST":
        #Traiter le formulaire
        nom=request.POST.get("username")
        mdp = request.POST.get("password")
        user=User.objects.create_user(username=nom,password=mdp)
        login(request,user)
        return redirect("index")
    return render(request,'compte/signup.html')

def login_user(request):
    if request.method=="POST":
        #CONNECTÉ L'USER
        nom = request.POST.get("username")
        mdp = request.POST.get("password")

        user = authenticate(username=nom,password=mdp)

        if user:
            login(request,user)
            return redirect('index')

    return render(request,'compte/login.html')

def logout_user(request):
    logout(request)
    return redirect('index')