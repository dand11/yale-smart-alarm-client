"""Exceptions for import."""


from typing import Any


class AuthenticationError(Exception):
    """Exception to indicate an issue with the authentication against the Yale Smart API."""

    def __init__(self, *args: Any) -> None:
        """Initialize the exception."""
        Exception.__init__(self, *args)

class HTTPError(Exception):
    """Exception to indicate an issue with the connection against the Yale Smart API."""

    def __init__(self, *args: Any) -> None:
        """Initialize the exception."""
        Exception.__init__(self, *args)

class ConnectError(Exception):
    """Exception to indicate an issue with the general connection."""

    def __init__(self, *args: Any) -> None:
        """Initialize the exception."""
        Exception.__init__(self, *args)
