from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

from django.shortcuts import redirect

default = lambda request: redirect('/customer/home')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include("customer.urls")),
    path('supplier/', include("supplier.urls")),
    path('', default)
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)