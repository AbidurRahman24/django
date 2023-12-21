from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    # path('signup/', views.signup, name='signup' ),
    path('signup/', views.SignupView.as_view(), name='signup' ),
    # path('login/', views.user_login, name='user_login' ),
    path('login/', views.UserLoginView.as_view(), name='user_login' ),
    path('logout/', views.user_logout, name='user_logout'),
    
]