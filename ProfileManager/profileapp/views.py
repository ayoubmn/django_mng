from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import LoginForm,SignupForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(redirect_field_name='login')
def Index(request):
    return render(request, 'index.html')

def Login(request):
    error = False
    if request.user.is_authenticated:
        return render(request, 'index.html')

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return render(request, 'index.html', locals())
            else: # sinon une erreur sera affichée
                error = True
    else:
        form = LoginForm()

    return render(request, 'login.html', locals())


def Signup(request):
    #print(request.__dict__)
    if request.user.is_authenticated():
        return render(request, 'index.html')

    form = SignupForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        envoi = True
        User.objects.create_user(username, email, password)
        return render(request, 'login.html')

    return render(request=request, template_name='signup.html', context={"register_form": form})


def Logout(request):
    logout(request)
    return redirect(reverse(connexion))


@login_required(redirect_field_name='login')
def Profile(request):
    return render(request, 'profile.html')
