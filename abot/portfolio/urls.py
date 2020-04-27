
from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='portfolio-home'),
    path('skills/', views.skillsData, name='portfolio-skillsData'),
]
