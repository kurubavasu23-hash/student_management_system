from django.contrib import admin
from django.urls import path, include
from stdmng import views

urlpatterns = [
    path("admin/", admin.site.urls),
   # path("", include("home.urls")),
     path("", include("stdmng.urls")),
]