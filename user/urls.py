from django.urls import path
from user import views

urlpatterns = [
    path('sign-up/', views.signup, name='sign-up'),
    path('sign-in/', views.signin, name='sign-in'),
    path('log-out/', views.logout_view, name='log-out')
]

