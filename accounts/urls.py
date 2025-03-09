from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accounts.views import CustomLoginView, CustomPasswordChangeView, SignUpView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', CustomPasswordChangeView.as_view(), name='password_change'),
    path('signup/', SignUpView.as_view(), name='signup')
]