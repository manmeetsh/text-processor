"""CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
 
""""""
urlpatterns = [
    #path('favsites', views.favsites, name='favsites'),
    # path('products/', views.products),
    # path('customer/', views.customer),
    #path('', include('accounts.urls'))
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('analyze/', views.analyze, name='analyze' ),
    # #path('home', views.home, name='home'),
    # path('rempunc', views.rempunc, name='rempunc'),
    # path('cap', views.cap, name='cap'),
    # path('linrem', views.linrem, name='linrem'),
    # path('spacrem', views.spacrem, name='spacrem'),
    # path('charcount', views.charcount, name='charcount'),

    

]
