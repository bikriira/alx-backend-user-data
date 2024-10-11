#!/usr/bin/env python3
"""Implementation of auth authentication system
"""
from typing import List, TypeVar
import os


class Auth:
    """ Manage the API authentication
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """_summary_

        Args:
            path (str)
            excluded_paths (List[str])

        Returns:
            bool
        """
        if path is None or not excluded_paths:
            return True

        path = path.rstrip("/") + "/"
        for exc_path in excluded_paths:
            if exc_path.endswith("*"):
                required_string = exc_path[:-1]
                if path.startswith(required_string):
                    return False
                else:
                    return True
            exc_path = exc_path.rstrip("/") + "/"
            if path == exc_path:
                return False
            else:
                return True

    def authorization_header(self, request=None) -> str:
        """_summary_

        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        else:
            return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """_summary_

        Returns:
            _type_: _description_
        """
        return None

    def session_cookie(self, request=None):
        """Return the session cookie value from the request.

        Args:
            request (optional): The request object containing cookies.
                                Defaults to None.

        Returns:
            str: The session cookie value, or None if not found or
                 request is None.
        """
        if not request:
            return None

        return request.cookies.get(os.getenv("SESSION_NAME"))
