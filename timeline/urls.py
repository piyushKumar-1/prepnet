
from django.urls import path
from . import views
from django.conf import settings

from django.conf.urls.static import static


app_name = "timeline"

urlpatterns = [
    path('upload/', views.add_Project, name='create'),
    path('timeline/', views.home_page, name='homepage'),
    path('profile/myprojects', views.my_projects, name='myprojects'),
    path('timeline/comments/<int:id>', views.read_comments, name='readcomments'),
    path('timeline/add-comment/<int:p_id>/', views.add_comment, name='addcomment'),
    path('timeline/project-details/<int:p_id>', views.project_details, name='projectdetails'),

]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)