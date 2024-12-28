from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mission/', views.mission_index, name='mission-index'),
    path('love/', views.love, name='love'),
    path('contact/',views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
]
