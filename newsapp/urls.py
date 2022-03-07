
from django.urls import path
from newsapp import views

urlpatterns = [    
    path('',views.home,name ='home'),   #url to redirect to home page bydefault
    path('search/',views.search,name ='search'),
]
