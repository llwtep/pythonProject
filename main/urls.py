
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='home'),
    path('contacts',views.contact,name='contacts'),
    path('about',views.about,name='about')
]