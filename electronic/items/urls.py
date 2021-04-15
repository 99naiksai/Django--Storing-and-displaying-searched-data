from django.urls import path
from items import views
urlpatterns = [
    path('laptop', views.laptop , name='laptop'),
    path('mobile' , views.mobile , name='mobile'),
    path('mobile_accessories' , views.mobile_accessories , name='mobile_accessories'),
    path('search' , views.search , name='search'),
    path('info' , views.info , name='info')

]