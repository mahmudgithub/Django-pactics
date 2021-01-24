from django.contrib import admin
from django.urls import path
from .views import one,two


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',one),
    path('',two),
]
