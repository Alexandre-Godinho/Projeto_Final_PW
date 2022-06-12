from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('aboutme/', views.aboutme_page_view, name='aboutme'),
    path('projects/', views.projects_page_view, name='projects'),
    path('projects/add_project/', views.add_project_view, name='add_project'),
    path('graduation/', views.graduation_page_view, name='graduation'),
    path('graduation/add_subject/', views.add_subject_view, name='add_subject'),
    path('blog/', views.blog_page_view, name='blog'),
    path('blog/add_post/', views.add_post_view, name='add_post'),
    path('blog/remove_post/<int:post_id>', views.remove_post_view, name='remove_post'),
]
