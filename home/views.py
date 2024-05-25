from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request, 'home/templates/home.html', {
        'username': request.user.username,
        'password': '********',  # Hasło jest maskowane
    })
