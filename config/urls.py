from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ocorrencias.urls')),
]


if settings.DEBUG:
    # Arquivos estáticos: CSS, JS etc.
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=None
    )

    # Arquivos enviados pelos usuários: fotos
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )