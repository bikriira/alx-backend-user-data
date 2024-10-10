#!/usr/bin/env python3
""" Implementation of basic_auth authentication system """
from pprint import pprint
from typing import TypeVar
from .auth import Auth
from base64 import b64decode
from models.user import User


class BasicAuth(Auth):
    """Basic Authentication class"""

    def extract_base64_authorization_header(
        self,
        authorization_header: str
    ) -> str:
        """
        Extracts the Base64 part of the Authorization header for Basic Auth.

        Args:
            authorization_header (str): The Authorization header value

        Returns:
            str: The Base64 part of the Authorization header
            None: If the header is invalid
        """
        if not authorization_header or not isinstance(
            authorization_header, str
        ):
            return None
        if not authorization_header.startswith("Basic "):
            return None
        else:
            return authorization_header[6:]

    def decode_base64_authorization_header(
        self,
        base64_authorization_header: str
    ) -> str:
        """
        Decodes the Base64 Authorization header.

        Args:
            base64_authorization_header (str): The Base64 Authorization header

        Returns:
            str: The decoded value as UTF8 string
            None: If it's not a valid Base64 string
        """
        if not base64_authorization_header or not isinstance(
            base64_authorization_header, str
        ):
            return None
        try:
            return b64decode(base64_authorization_header).decode("utf-8")
        except Exception:
            return None

    def extract_user_credentials(
        self,
        decoded_base64_authorization_header: str
    ) -> (str, str):
        """
        Extracts user credentials from the decoded Base64 Authorization header.

        Args:
            decoded_base64_authorization_header (str): Decoded header

        Returns:
            tuple: A tuple containing the user email and password
            (None, None): If the decoded_base64_authorization_header is invalid
        """
        if not decoded_base64_authorization_header or not isinstance(
            decoded_base64_authorization_header, str
        ):
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(":", 1))

    def user_object_from_credentials(self, user_email: str, user_pwd: str) \
            -> TypeVar('User'):
        """Retrieve a User object based on email and password.

        Args:
            user_email (str): The email of the user.
            user_pwd (str): The password of the user.

        Returns:
            User: The User object if the credentials are valid.
            None: If the email or password is invalid, or no user found.
        """
        if not user_email or not user_pwd or not \
                isinstance(user_email, str) or not isinstance(user_pwd, str):
            return None
        try:
            user = User.search({"email": user_email})[0]
        except Exception as e:
            return None

        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar('User'):
        """Retrieve the current user based on the request.

        This method extracts the user's credentials from the request's 
        authorization header, decodes them, and validates them against 
        the stored user data. If the credentials are valid, the corresponding 
        User object is returned. If the credentials are invalid or missing, 
        None is returned.

        Args:
            request: The incoming request object, which may contain the 
                    Authorization header needed for authentication.

        Returns:
            User: The User object associated with the provided credentials 
                if they are valid; otherwise, returns None.
        """
        encoded_credentials = self.authorization_header(request)
        parsed_credentials = self.extract_base64_authorization_header(
            encoded_credentials)
        decoded_credentials = self.decode_base64_authorization_header(
            parsed_credentials)
        user_credentials = self.extract_user_credentials(decoded_credentials)
        user_object = self.user_object_from_credentials(*user_credentials)

        return user_object
