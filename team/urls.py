from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "team"

urlpatterns = [
    path('timeline/team/',views.team, name='team'),
    path('timeline/team/myteam',views.myteam, name='myteam'),
    path('timeline/team/allteams/',views.show_all, name='allteam'),
    path('timeline/team/allteams/<int:id>/details/',views.team_details, name='team_deatils'),
    path('timeline/team/member_skill/<int:size>/<int:i>/<int:id>',views.skills, name='skill')

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
