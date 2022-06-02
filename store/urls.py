from argparse import Namespace
from django import views
from django.urls import path
from .views import (index , shop, blog, about, contact)

app_name = 'cara'

urlpatterns = [
    path('', index , name='index' ),
    path('shop/', shop , name='shop' ),
    path('blog/', blog , name='blog' ),
    path('about/', about , name='about' ),
    path('contact/', contact , name='contact' ),

]
