from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "profiles"

urlpatterns = [
    path('myprofile/', views.my_profile, name='myprofile'),
    path('search/', views.search_profile, name='searchprofile')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
