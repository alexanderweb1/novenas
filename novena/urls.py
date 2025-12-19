from django.urls import path
from . import views
from .views import novena_diaN, novena_diaC

app_name = 'novena'

urlpatterns = [
    path('', views.home, name='home'),
    path('virgenC/', views.virgenC, name='virgenC'),
    path('divinoN/', views.divinoN, name='divinoN'),
    
    path('nino/<str:novena>/<int:dia>/', views.novena_diaN, name='novena_diaN'),
    path('cisne/<str:novena>/<int:dia>/', views.novena_diaC, name='novena_diaC'),

]