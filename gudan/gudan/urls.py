from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Icy Delight's Admin"
admin.site.site_title = "Icy Delight's Admin Portal"
admin.site.index_title = "Welcome to Icy Delight"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name='home'),
    path("about",views.about,name='about'),
    path("services",views.services,name='services'),
    path("contact",views.contact,name='contact'),
]
