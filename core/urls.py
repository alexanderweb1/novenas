from django.contrib import admin
from django.urls import path, include
from novena import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('novena/', include('novena.urls', namespace='novena')),

]
