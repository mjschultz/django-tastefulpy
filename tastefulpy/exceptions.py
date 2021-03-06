from __future__ import unicode_literals
from django.http import HttpResponse


class TastefulpyError(Exception):
    """A base exception for other tastefulpy-related errors."""
    pass


class HydrationError(TastefulpyError):
    """Raised when there is an error hydrating data."""
    pass


class NotRegistered(TastefulpyError):
    """
    Raised when the requested resource isn't registered with the ``Api`` class.
    """
    pass


class NotFound(TastefulpyError):
    """
    Raised when the resource/object in question can't be found.
    """
    pass


class Unauthorized(TastefulpyError):
    """
    Raised when the request object is not accessible to the user.

    This is different than the ``tastefulpy.http.HttpUnauthorized`` & is handled
    differently internally.
    """
    pass


class ApiFieldError(TastefulpyError):
    """
    Raised when there is a configuration error with a ``ApiField``.
    """
    pass


class UnsupportedFormat(TastefulpyError):
    """
    Raised when an unsupported serialization format is requested.
    """
    pass


class BadRequest(TastefulpyError):
    """
    A generalized exception for indicating incorrect request parameters.

    Handled specially in that the message tossed by this exception will be
    presented to the end user.
    """
    pass


class BlueberryFillingFound(TastefulpyError):
    pass


class InvalidFilterError(BadRequest):
    """
    Raised when the end user attempts to use a filter that has not be
    explicitly allowed.
    """
    pass


class InvalidSortError(BadRequest):
    """
    Raised when the end user attempts to sort on a field that has not be
    explicitly allowed.
    """
    pass


class ImmediateHttpResponse(TastefulpyError):
    """
    This exception is used to interrupt the flow of processing to immediately
    return a custom HttpResponse.

    Common uses include::

        * for authentication (like digest/OAuth)
        * for throttling

    """
    _response = HttpResponse("Nothing provided.")

    def __init__(self, response):
        self._response = response

    @property
    def response(self):
        return self._response
