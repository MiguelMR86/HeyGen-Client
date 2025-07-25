from http import HTTPStatus
from unittest.mock import Mock

import pytest
from requests import HTTPError

from error_handlers import heygen_request_error_handler
from exceptions import HeygenAPIError, HeygenUnexpectedError


class TestHeygenRequestErrorHandler:
    def setup_method(self):
        self.error_message = "test message"

    def test_heygen_request_error_handler(self):
        mock_response = Mock()
        mock_response.status_code = HTTPStatus.BAD_REQUEST
        mock_response.json.return_value = {"error": self.error_message}

        @heygen_request_error_handler
        def test_function():
            raise HTTPError(response=mock_response)

        with pytest.raises(HeygenAPIError) as e:
            test_function()

        assert e.value.status_code == HTTPStatus.BAD_REQUEST
        assert e.value.message == self.error_message

    def test_heygen_request_error_handler_with_non_json_response(self):
        mock_response = Mock()
        mock_response.status_code = HTTPStatus.BAD_REQUEST
        mock_response.text = self.error_message
        mock_response.json.side_effect = ValueError()

        @heygen_request_error_handler
        def test_function():
            raise HTTPError(response=mock_response)

        with pytest.raises(HeygenAPIError) as e:
            test_function()

        assert e.value.status_code == HTTPStatus.BAD_REQUEST
        assert e.value.message == self.error_message

    def test_heygen_request_error_handler_with_unexpected_error(self):
        @heygen_request_error_handler
        def test_function():
            raise Exception(self.error_message)

        with pytest.raises(HeygenUnexpectedError) as e:
            test_function()

        assert e.value.message == self.error_message
