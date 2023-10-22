from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

UserModel = get_user_model()

def custom_validation(data):
    email = data.get('email', '').strip()
    username = data.get('username', '').strip()
    password = data.get('password', '').strip()

    if not email:
        raise ValidationError('Um email é necessário')
    
    if UserModel.objects.filter(email=email).exists():
        raise ValidationError('Escolha outro email')

    if not username:
        raise ValidationError('Um nome de usuário é necessário')
    
    if not password:
        raise ValidationError('Uma senha é necessária')
    
    return data


def validate_email(data):
    email = data['email'].strip()
    if not email:
        raise ValidationError('Um email necessario')
    return True

def validate_username(data):
    username = data['username'].strip()
    if not username:
        raise ValidationError('Usuario necessario ')
    return True

def validate_password(data):
    password = data['password'].strip()
    if not password:
        raise ValidationError('Senha necessaria?')
    return True