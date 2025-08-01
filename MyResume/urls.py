from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path,include
from index import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = []

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns+= i18n_patterns(
    path('admin/', admin.site.urls),
    path('', views.index.as_view()),
    path('rosetta',include('rosetta.urls')),
    prefix_default_language=False
)
