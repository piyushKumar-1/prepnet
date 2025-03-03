from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "codetest"

urlpatterns = [
    path('timeline/test/',views.test, name='test'),
    path('profile/mytest',views.mytest, name='mytest'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
