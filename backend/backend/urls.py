from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(title='API Docs - Cardord Carshop')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api/schema/', schema_view),
    path('api/docs/', include_docs_urls(title='API Docs')),
]
