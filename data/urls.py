from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_page,name='main_page'),
    path('received_data/',views.received_data,name='received_data'),
    path('received_data/<int:pk>/',views.extended_info,name='extended_info'),
]
