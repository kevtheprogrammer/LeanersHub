from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from acc.views import HomePage

urlpatterns = [
    path("",HomePage ,name='home'),
    path("admin/", admin.site.urls),
    path("account/",include('acc.urls')),
    path("courses/",include('courses.urls')),
    path("assessments/",include('assessments.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
