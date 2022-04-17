from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views


app_name = 'bodrum'


urlpatterns =[
    path('',views.index,name ='index'),
    path('about/',views.about,name='about'),
    path('our-parthners/',views.company,name='our-parthners'),
    path('gallery/',views.gallery,name='gallery'),
]
