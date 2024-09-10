#!/usr/bin/env python3
"""template for all authentication system
"""
from typing import List, TypeVar
from flask import request


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
        if path in excluded_paths:
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


class BasicAuth(Auth):
    """_summary_

    Args:
        Auth (_type_): _description_
    """
    pass
