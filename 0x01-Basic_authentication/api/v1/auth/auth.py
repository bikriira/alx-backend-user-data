#!/usr/bin/env python3
"""Implementation of auth authentication system
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
        for exc_path in excluded_paths:
            if exc_path.endswith("*"):
                required_string = exc_path[:-2]
                if path.startswith(required_string):
                    return False
                else:
                    return True
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
