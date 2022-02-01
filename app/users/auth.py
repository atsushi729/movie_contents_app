import datetime
from jose import jwt, ExpiredSignatureError
from app import config

from .models import User

settings = config.get_settings()


def authenticate(email, password):
    # 1st step
    try:
        user_obj = User.objects.get(email=email)  # if user does not exist throw exception
    except Exception as e:
        user_obj = None
    if not user_obj.verify_password(password):  # if users password is not correct throw return None
        return None
    return user_obj


def login(user_obj, expires=5):  # create token if user passed 1st step
    # 2nd step
    raw_data = {
        "user_id": f"{user_obj.user_id}",
        "role": "admin",
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=expires)
    }
    return jwt.encode(raw_data, settings.secret_key, algorithm=settings.jwt_algorithm)


def verify_user_id(token):
    # 3rd step
    data = {}
    try:
        data = jwt.decode(token, settings.secret_key, algorithms=[settings.jwt_algorithm])
    except ExpiredSignatureError as e:
        print(e)
    except:
        pass
    if 'user_id' not in data:
        return None
    return data
