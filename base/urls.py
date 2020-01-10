from django.contrib import admin
from django.urls import path, include
from .views import index, glogin, submit, glogout

app_name = 'base'

urlpatterns = [
    path('admin', admin.site.urls),
    path('agenda', include('agenda.urls', namespace='agenda')),
    path('servicos', include('servicos.urls', namespace='servicos')),
    path('index', index, name='index'),
    path('', glogin, name='login'),
    path('logout', glogout, name='logout'),
    path('submit', submit, name='submit'),
]
