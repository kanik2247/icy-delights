from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "Kanika's Ice Creams Admin"
admin.site.site_title = "Kanika's Ice Creams Admin Portal"
admin.site.index_title = "Welcome to Kanika's Ice Creams"

urlpatterns = [
    path('admin/', admin.site.urls),
     path('',include('home.urls')),
]
