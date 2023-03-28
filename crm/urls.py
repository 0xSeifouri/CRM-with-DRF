from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_data, name='create'),
    path('show/<int:pk>/', views.retrieve_data, name='retrieve'),
    path('update/<int:pk>/', views.update_data, name='update'),
    path('delete/<int:pk>/', views.delete_data, name='destroy'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    path('api/list/', views.ShowAll.as_view(), name='list'),
    path('api/create/', views.Create.as_view(), name='api-create'),
    path('api/show/<int:pk>/', views.Retrieve.as_view(), name='api-retrieve'),
    path('api/update/<int:pk>/', views.Update.as_view(), name='api-update'),
    path('api/delete/<int:pk>/', views.Destroy.as_view(), name='api-destroy'),



]
