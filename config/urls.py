from django.contrib import admin
from django.urls import path
from core.views import home, about


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
]