from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from api import views  # Import your API views here
from django.conf import settings
from django.conf.urls.static import static


from django.contrib import admin
from django.urls import path, include


schema_view = get_schema_view(
    openapi.Info(
        title="Fan Engagement and Management API",
        default_version='v1',
        description="API documentation for the fan engagement and management system",
        terms_of_service="https://www.yourclubsite.com/terms/",
        contact=openapi.Contact(email="support@yourclubsite.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),  # Set permission class as needed
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/tickets/', include('tickets.urls')),  # Include tickets app URLs
    path('api/payments/', include('payments.urls')),
    path('api/memberships/', include('membership.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

