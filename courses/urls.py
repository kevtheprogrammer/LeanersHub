from django.urls import path,include

from .views import *
app_name = 'courses'

urlpatterns = [
    path("", CourserIndexScreen.as_view(),name='index' ),
]

 
 