from django.urls import path
from .views import SignUpView,Login


account_patterns = [
    path('signup/', SignUpView.as_view(), name="signup"),
    path('login/', Login.as_view(), name="login"),


]