#!/usr/bin/env python3
""" Implementation of basic_auth authentication system """
from .auth import Auth
from base64 import b64decode


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
