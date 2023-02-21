from django.urls import path
from cars import views
urlpatterns = [

    # Paths for cars
    path('', views.car_list, name='car_list'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('car/new/', views.car_create, name='car_create'),
    path('car/<int:car_id>/edit/', views.car_update, name='car_update'),
    path('car/<int:car_id>/delete/', views.car_delete, name='car_delete'),

    # Path for pilots
    path('driver/', views.driver_list, name='driver_list'),
    path('driver/<int:driver_id>/', views.driver_detail, name='driver_detail'),
    path('driver/new/', views.driver_create, name='driver_create'),
    path('driver/<int:driver_id>/edit/', views.driver_update, name='driver_update'),
    path('driver/<int:driver_id>/delete/', views.driver_delete, name='driver_delete'),
]
