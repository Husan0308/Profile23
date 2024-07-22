from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('signup/', views.signup_user, name="signup"),
    path('login/', views.login_user, name="login"),
    path('home/', views.home, name="home"),    
    path('add/', views.add, name="add"),
    path('save-personal/', views.save_personal, name="save_personal"),
    path('save_skill_box/', views.save_skill_box, name="save_skill_box"),
    path('save_education_box/', views.save_education_box, name="save_education_box"),
    path('save_language_box/', views.save_language_box, name="save_language_box"),
    path('save_profile_box/', views.save_profile_box, name="save_profile_box"),
    path('save_experience_box/', views.save_experience_box, name="save_experience_box"),
    path('save_interest_box/', views.save_interest_box, name="save_interest_box"),
]