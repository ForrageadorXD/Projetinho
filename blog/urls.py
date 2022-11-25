from django.contrib import admin
from django.urls import path
from postagem.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name="index"),
    path('loja/',loja,name="loja"),
    path('quemsomos/',quemsomos,name="quemsomos"),
    path('aventura/',aventura,name="aventura"),
    path('fps/',fps,name="fps"),
    path('detalhes/<int:id>',detalhes,name="detalhes"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)