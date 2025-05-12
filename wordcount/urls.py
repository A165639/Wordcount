
from django.contrib import admin
from django.urls import path
from . import view

urlpatterns = [
    #ath("admin/", admin.site.urls),
    path('',view.homepage, name='home'),
    path('countbb/',view.count,   name='count'),
    path('about/',view.about, name='about'),
    path('contact/',view.contact, name='contact'),
]
