from django.urls import path, include
from user.views import *

# 127.0.0.1:8000/user/

urlpatterns = [
    # Templates

    path("home/", home, name="home"),

    # API

    # Gmail code
    path('api/v1/send_email/', SentEmailToGmail.as_view({'post': 'create'})),
    path('api/v1/check_email/', LoginCodeView.as_view({'post': 'create'})),
    # path('token/', LoginTokenView.as_view()),
    # path('send/email/', SentEmailToGmail.as_view({'post': 'create'})),
    # path('check/code/', LoginCodeView.as_view({'post': 'create'})),
]
