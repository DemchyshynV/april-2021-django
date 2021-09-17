from django.urls import path

from .views import AutoParkCarListCreateView, AutoParkListCreateView, AutoParkRetrieveDestroyView

urlpatterns = [
    path('', AutoParkListCreateView.as_view(), name='auto_park_list_create'),
    path('/<int:pk>', AutoParkRetrieveDestroyView.as_view(), name='auto_park_retrieve_destroy'),
    path('/<int:pk>/cars', AutoParkCarListCreateView.as_view(), name='auto_park_by_id_car_list_create')

]
