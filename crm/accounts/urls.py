from .views import *
from django.urls import path
import knox.views as knox_views

urlpatterns = [
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('check/', CheckAuthentication.as_view(), name='check_auth'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),

]