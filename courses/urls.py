from django.urls import path,include

from .views import *
app_name = 'courses'

urlpatterns = [
    path("", CourserIndexView.as_view(),name='index' ),
    path("<str:slug>/", CourserDetailView.as_view(),name='couse-outline' ),
    path("<str:slug1>/<str:slug>/", CourserLessonDetailView.as_view(),name='lesson' ),
    path("pricing", CourcePricingIndex.as_view(),name='pricing' ),
]

 
 