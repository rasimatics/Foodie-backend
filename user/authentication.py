import jwt
from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication
from core import settings
from .models import User


class JWTAuthentication(BaseAuthentication):
    keyword = "CToken"

    def authenticate(self, request):
        header = request.headers.get('Authorization').split()

        if not header or header[0].lower() != self.keyword.lower():
            return None

        if len(header) == 1:
            raise exceptions.AuthenticationFailed("Invalid token header")

        elif len(header) > 2:
            raise exceptions.AuthenticationFailed("Invalid token header")

        try:
            access_token = header[1]
            payload = jwt.decode(access_token, settings.SECRET_KEY, algorithms='HS256')

        except jwt.exceptions.ImmatureSignatureError:
            raise exceptions.AuthenticationFailed("Access token invalid")

        except jwt.exceptions.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("Access token invalid")

        except jwt.exceptions.DecodeError:
            raise exceptions.AuthenticationFailed("Access token invalid")

        except IndexError:
            raise exceptions.AuthenticationFailed("Token prefix missing")

        user = User.objects.filter(id=payload['id'], username=payload['username']).first()

        if user is None:
            raise exceptions.AuthenticationFailed("User not found")

        return user, access_token
