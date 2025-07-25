import logging
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

from requests import HTTPError

from exceptions import HeygenAPIError, HeygenUnexpectedError

logger = logging.getLogger(__name__)

P = ParamSpec("P")
R = TypeVar("R")


def heygen_request_error_handler(func: Callable[P, R]) -> Callable[P, R]:
    @wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        try:
            return func(*args, **kwargs)
        except HTTPError as e:
            try:
                error_payload = e.response.json()
                message = error_payload.get("error", str(e))
            except ValueError:
                message = e.response.text or str(e)

            logger.error(f"API error: {message}")
            raise HeygenAPIError(
                message=message, status_code=e.response.status_code
            ) from e
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            raise HeygenUnexpectedError(message=str(e)) from e

    return wrapper
