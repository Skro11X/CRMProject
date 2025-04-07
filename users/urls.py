from django.urls import path
from django.contrib.auth.views import LoginView
from users.views import SignUpUser


urlpatterns = [
    path('sign_up/', SignUpUser.as_view(), name="sign_up"),
]