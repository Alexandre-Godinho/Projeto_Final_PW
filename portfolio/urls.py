from django.urls import path
from . import views

app_name = "portfolio"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('aboutme/', views.aboutme_page_view, name='aboutme'),
    path('projects/', views.projects_page_view, name='projects'),
    path('graduation/', views.graduation_page_view, name='graduation'),
    path('blog/', views.blog_page_view, name='blog'),
    path('blog/add_post/', views.add_post_view, name='add_post'),
]
