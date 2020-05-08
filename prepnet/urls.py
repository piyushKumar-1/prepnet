from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

def yo(request):

    return HttpResponse("something")



urlpatterns = [
    path('', include("codetest.urls")),
    path('', include("prep.urls")),
    path('', include("team.urls")),
    path('', include("timeline.urls")),
    path('', include("profiles.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls"))
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
