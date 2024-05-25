from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('django.contrib.auth.urls')),  # Dodaj to, aby obsłużyć logowanie
    path('', include('home.urls')),
]
