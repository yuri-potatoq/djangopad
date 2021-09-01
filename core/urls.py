from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    # api views
    path('v1/', include('core_auth.urls')),

    # dashboard views
    path('', include('dashboard.dashboard.urls')),
    path('', include('dashboard.login.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
