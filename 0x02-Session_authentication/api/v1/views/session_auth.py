#!/usr/bin/env python3
"""
User login endpoint.

This function handles user authentication. It accepts an email and
password, and if valid, creates a session and sets a session cookie.

Endpoint:
    POST /auth_session/login

Returns:
    JSON response with user info or error messages.

Example:
    {
        "email": "user@example.com",
        "password": "userpassword"
    }
"""

from api.v1.views import app_views
from flask import request, jsonify, make_response
from models.user import User
import os


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def login():
    """Handles user login and session creation.

    This route allows a user to log in by providing their email
    and password. Upon successful authentication, a session ID
    is created, and the session cookie is set in the response.

    Args:
        None

    Returns:
        Response: A JSON response containing user information or
                  error messages with appropriate HTTP status codes.
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if not email:
        return jsonify({"error": "email missing"}), 400
    if not password:
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})

    if not user:
        return jsonify({"error": "no user found for this email"}), 404

    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth

    session_id = auth.create_session(user.id)
    response = make_response(user.to_json())
    response.set_cookie(os.getenv("SESSION_NAME"), session_id)
    return response
