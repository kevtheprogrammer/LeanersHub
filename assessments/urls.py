from django.urls import path,include

from .views import *
app_name = 'assessment'

urlpatterns = [
    path("<int:pk>/", CourserTestDetailView.as_view(),name='test' ),
]