from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext as _

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('yasg.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.site_header = _('Project Name')
admin.site.site_title = _('Project Name')
admin.site.index_title = _('Project Name')
