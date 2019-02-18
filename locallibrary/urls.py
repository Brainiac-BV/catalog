from django.contrib import admin
from django.urls import path
from django.urls import include
#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
from django.conf import settings
# Use static() to add url mapping to serve static files during development (only)
from django.conf.urls.static import static
from catalog.views import home_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls')),
    path('', home_view),# RedirectView.as_view(url='/catalog/', permanent=True)),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

