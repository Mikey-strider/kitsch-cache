from django.urls import path
from . import views # Import views to connect routes to view functions

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('mission/', views.mission_index, name='mission-index'),
    path('love/', views.love, name='love'),
    path('contact/',views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('anita', views.anita, name='anita'),
    path('deena', views.deena, name='deena'),
    path('denise', views.denise, name='denise'),
    path('robin', views.robin, name='robin'),
    path('sandra', views.sandra, name='sandra'),
]
