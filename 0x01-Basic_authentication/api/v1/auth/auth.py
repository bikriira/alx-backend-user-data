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
        return False

    def authorization_header(self, request=None) -> str:
        """_summary_

        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            str: _description_
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """_summary_

        Returns:
            _type_: _description_
        """
        return None
