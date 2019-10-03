from django.urls import path

from FRS.views import FlightList, FlightDetail, UserCreate, LoginView

urlpatterns = [
    path('flights/', FlightList.as_view()),
    path('flights/<int:pk>/', FlightDetail.as_view(), name='flightdetail'),
    path('users/', UserCreate.as_view(), name='account-create'),
    path('login/', LoginView.as_view(), name='account-login'),
]
