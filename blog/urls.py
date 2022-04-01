from django.urls import path
from blog import views

urlpatterns = [
    path('home/',views.home_view,name='home'),
    path('',views.login_with_google_view,name='login'),
]