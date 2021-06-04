
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("books.urls")), # Books App Urls.
    path('api/', include("api.urls")), # Api Urls.
]
