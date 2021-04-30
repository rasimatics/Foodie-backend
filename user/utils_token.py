import jwt
import datetime
from core import settings
from rest_framework import exceptions
from .models import User


def generate_token(user):
    payload = {
        'id': user.id,
        'username': user.username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, minutes=10),
        'iat': datetime.datetime.utcnow()
    }

    access_token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return access_token


def generate_refresh_token(user):
    payload = {
        'id': user.id,
        'username': user.username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=7),
        'iat': datetime.datetime.utcnow()
    }

    refresh_token = jwt.encode(payload, settings.REFRESH_TOKEN_SECRET, algorithm='HS256')
    return refresh_token


def new_token_after_refresh(refresh_token):
    try:
        payload = jwt.decode(
            refresh_token,
            settings.REFRESH_TOKEN_SECRET,
            algorithms=['HS256']
        )
    except jwt.ExpiredSignatureError:
        raise exceptions.AuthenticationFailed('Expired refresh token. Request new pair.')
    except jwt.exceptions.InvalidSignatureError:
        raise exceptions.AuthenticationFailed('Invalid refresh token. Request a valid token pair.')

    user = User.objects.filter(id=payload.get('id')).first()

    if user is None:
        raise exceptions.AuthenticationFailed('User not found.')

    return generate_token(user)
