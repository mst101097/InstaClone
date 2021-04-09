from django.urls import path
from authentication.views import (
    SignUpView ,
    SignInView
    )

urlpatterns = [
    path('', SignInView.as_view(), name = 'signin_view'),
    path('signup/', SignUpView.as_view(), name = 'signup_view'),

]