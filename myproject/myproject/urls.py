
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = "Divyansh Admin"
admin.site.site_title = "Divyansh Admin"
admin.site.index_title = "Welcome to Divyansh Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("myapp.urls")),
]
