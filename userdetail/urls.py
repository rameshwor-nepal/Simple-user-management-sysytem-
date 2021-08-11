from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adduser/', views.adduser, name='adduser'),
    path('detail/<int:id>', views.detail, name = 'detailuser'),
    path('update/<int:id>', views.update, name = 'updateuser'),    
    path('detail/<int:id>/delete', views.delete, name = 'deleteuser'),
]