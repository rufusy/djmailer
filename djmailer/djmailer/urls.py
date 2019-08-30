from django.contrib import admin
from django.urls import path, include

from api import urls as apiUrls

urlpatterns = [
    path('api/', include(apiUrls, namespace='api')),
    path('admin/', admin.site.urls),
]
