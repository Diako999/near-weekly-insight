from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('transactions/', include('transactions.urls')),
    path('blocks/', include('blocks.urls')),
]
