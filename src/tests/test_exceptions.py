from http import HTTPStatus

from exceptions import HeygenAPIError, HeygenUnexpectedError


class TestHeygenAPIError:
    def test_initialization(self):
        message = "Test API error"
        status_code = HTTPStatus.BAD_REQUEST
        error = HeygenAPIError(message=message, status_code=status_code)

        assert error.message == message
        assert error.status_code == status_code
        assert str(error) == f"{HeygenAPIError.error_prefix} {message}"


class TestHeygenUnexpectedError:
    def test_initialization(self):
        message = "Test unexpected error"
        error = HeygenUnexpectedError(message=message)

        assert error.message == message
        assert str(error) == f"{HeygenUnexpectedError.error_prefix} {message}"
