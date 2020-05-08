from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "prep"



urlpatterns = [
    path('',views.home, name='home'),
    path('signup/', views.RegisterView.as_view(), name="signup"),
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/',views.LogoutView.as_view(), name='logout'),
    path('construction/', views.construction, name='construction'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


'''
urlpatterns = [
    path('',views.home, name='home'),
    path('signup/', views.sign_up, name="signup"),
    path('login/', views.log_in, name="login"),
    path('logout/',views.log_out, name='logout'),
]



'''