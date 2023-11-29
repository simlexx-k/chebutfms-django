from .views import generate_farmer_list_pdf, login_view, tea_submission_view, dashboard_view, landing_view
from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('generate_farmer_list_pdf/', generate_farmer_list_pdf, name='generate_farmer_list_pdf'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('tea_submission/', tea_submission_view, name="tea_submission"),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('landing/', landing_view, name='landing'), 
]



