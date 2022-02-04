from fastapi import HTTPException


class LoginRequiredException(HTTPException):
    pass


class UserHasAccountException(Exception):
    """
    User already has account.
    """


class InvalidEmailException(Exception):
    """
    Invalid email
    """


class InvalidUserIDException(Exception):
    """
    Invalid User ID
    """
