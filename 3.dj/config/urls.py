
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404

handler404 = 'app.views.page_not_found'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]
