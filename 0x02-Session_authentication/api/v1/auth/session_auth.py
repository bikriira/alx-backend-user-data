#!/usr/bin/env python3
"""Session authentication module"""
from .auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """Session authentication class"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Creates a session ID for a given user_id.

        Args:
            user_id (str): The ID of the user.

        Returns:
            str: The generated session ID or None if user_id is invalid.
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None

        # Generate a new session ID
        session_id = str(uuid.uuid4())

        # Store the user_id associated with the session_id
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Retrieve the user ID associated with a given session ID.

        Args:
            session_id (str, optional): The session ID to look up.
                                        Defaults to None.

        Returns:
            str: The user ID associated with the session ID,
                 or None if the session ID is invalid or not found.
        """
        if not session_id or not isinstance(session_id, str):
            return None
        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        Retrieve the current user based on the session ID from the request.

        Args:
            request (optional): The HTTP request object containing cookies.

        Returns:
            User: The user object corresponding to the request's session ID,
                  or None if no valid session is found.
        """
        session_id = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_id)
        user = User.get(user_id)

        return user

    def destroy_session(self, request=None):
        """Destroy a session based on the request.

        Args:
            request: The request object containing the session cookie.

        Returns:
            bool: True if the session was successfully destroyed,
                  False otherwise.
        """
        if not request:
            return False

        session_id = self.session_cookie(request)

        if not session_id or not self.user_id_for_session_id(session_id):
            return False

        del self.user_id_by_session_id[session_id]

        return True
