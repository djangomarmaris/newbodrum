from django.urls import path
from django.utils.translation import gettext_lazy as _

from . import views


app_name = 'bodrum'


urlpatterns =[
    path('',views.index,name ='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('our-parthners/',views.company,name='our-parthners'),
    path('gallery/',views.gallery,name='gallery'),
    #path('categorys/',views.list,name='list'),
    path('<str:category_slug>/',views.Show,name='category_list'),
    path('otel/<str:category_slug>/',views.otelShow,name='otel_list'),
    path('endüs/<str:category_slug>/',views.enShow,name='endüs_list'),
    path('open/<str:category_slug>/',views.openShow,name='open_list'),
    path('<str:slug>/<int:id>/',views.detail,name='product_detail'),
]
