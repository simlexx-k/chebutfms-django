from .views import submit_tea, success_page
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('submit_tea/', submit_tea, name='submit_tea'),
    path('success_page/', success_page, name='success_page'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

