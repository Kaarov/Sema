from datetime import datetime
import random

from django.core.mail import send_mail
from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from Sema import settings
from user.models import User


# Templates
def home(request):
    return render(request, 'Base/home.html')


# API


# Check Email Password from Gmail
class SentEmailToGmail(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data['name']
        email = request.data['email']
        code = str(random.randint(1000, 9999))
        now = datetime.now()

        user = User.objects.filter(username=username)
        if user:
            user = user[0]
            if user.attempt <= 4:
                if len(email) > 0:
                    receiver_address = email
                    mail_content = f"{username} your password is {code}!\n You have {5 - user.attempt} attempts"

                    send_mail(
                        subject='Here is your password',
                        message=mail_content,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[receiver_address]
                    )
                    if user.code:
                        user.code = ''
                    user.attempt += 1
                    user.code = code
                    user.email = email
                    user.save()

                    return Response({
                        'success': f"The message was sent successfully! You have {6 - user.attempt} attempts!"
                    })

                return Response({
                    'error': "Check your gmail login please!"
                })
            else:
                return Response({
                    "error": "You cannot recieve a password!"
                })
        else:
            new_user = User(date_joined=now, username=username, is_active=True, email=email, code=code,
                            role="student", attempt=1)
            new_user.save()
            receiver_address = email
            mail_content = f"{username} your password is {code}!\n You have {6 - new_user.attempt} attempts"

            send_mail(
                subject='Here is your password',
                message=mail_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[receiver_address]
            )
            return Response({
                'success': f"The message was sent successfully! You have {6 - new_user.attempt} attempts!"
            })


class LoginCodeView(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        username = request.data['name']
        password = request.data['password']
        email = request.data['email']
        code = request.data['code']
        user = User.objects.get(username=username, code=code)
        now = datetime.now()

        if username == user.username and email in user.email and code in user.code:
            token = Token.objects.filter(user=user)
            if token:
                token.delete()
            token = Token(user=user)
            token.save()
            if user.code:
                user.code = ''
                user.save()
            if user.last_login:
                user.last_login = ''
                user.save()
            user.last_login = now
            user.role = "student"
            user.set_password(password)
            user.save()
            return Response({
                'token': token.key,
                'user_id': user.id
            })
        else:
            return Response({
                'error': "Code or Email not correct"
            })
