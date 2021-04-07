from django.urls import path
from authentication.views import SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name = 'signup_view'),

]