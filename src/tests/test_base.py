from http import HTTPStatus

import pytest

from base import HeygenBaseClient
from exceptions import HeygenAPIError

TEST_URL = "http://localhost:8000/test_endpoint"
MOCK_POST_PAYLOAD = {"text": "Hello, world!"}

MOCK_SUCCESS_RESPONSE = {"code": 0, "error": None, "data": {"video_id": "12345"}}
MOCK_ERROR_RESPONSE = {"code": 1, "error": "Error message", "data": None}


class TestHeygenBaseClient:
    def test_get_success(self, requests_mock):
        """
        GIVEN a HeygenBaseClient instance
        WHEN the get method is called and the API returns a successful response
        THEN it should return the correct JSON data
        AND make a request with the correct URL, method, and headers.
        """
        requests_mock.get(
            TEST_URL, json=MOCK_SUCCESS_RESPONSE, status_code=HTTPStatus.OK
        )
        client = HeygenBaseClient()
        response = client.get(url=TEST_URL)
        assert response.json() == MOCK_SUCCESS_RESPONSE

    def test_get_error(self, requests_mock):
        """
        GIVEN a HeygenBaseClient instance
        WHEN the get method is called and the API returns a JSON error
        THEN it should raise a HeygenAPIError with the correct status and message.
        """
        requests_mock.get(
            TEST_URL, json=MOCK_ERROR_RESPONSE, status_code=HTTPStatus.BAD_REQUEST
        )
        client = HeygenBaseClient()

        with pytest.raises(HeygenAPIError) as e:
            client.get(url=TEST_URL)

        assert e.value.status_code == HTTPStatus.BAD_REQUEST
        assert e.value.message == MOCK_ERROR_RESPONSE["error"]

    def test_post_success(self, requests_mock):
        """
        GIVEN a HeygenBaseClient instance
        WHEN the post method is called and the API returns a successful response
        THEN it should return the correct JSON data
        AND make a request with the correct URL, method, headers, and payload.
        """
        requests_mock.post(
            TEST_URL, json=MOCK_SUCCESS_RESPONSE, status_code=HTTPStatus.OK
        )
        client = HeygenBaseClient()
        response = client.post(url=TEST_URL, payload=MOCK_POST_PAYLOAD)
        assert response.json() == MOCK_SUCCESS_RESPONSE

    def test_post_error(self, requests_mock):
        """
        GIVEN a HeygenBaseClient instance
        WHEN the post method is called and the API returns a JSON error
        THEN it should raise a HeygenAPIError with the correct status and message.
        """
        requests_mock.post(
            TEST_URL, json=MOCK_ERROR_RESPONSE, status_code=HTTPStatus.BAD_REQUEST
        )
        client = HeygenBaseClient()
        with pytest.raises(HeygenAPIError) as e:
            client.post(url=TEST_URL, payload=MOCK_POST_PAYLOAD)

        assert e.value.status_code == HTTPStatus.BAD_REQUEST
        assert e.value.message == MOCK_ERROR_RESPONSE["error"]

    def test_failure_with_non_json_response(self, requests_mock):
        """
        GIVEN a HeygenBaseClient instance
        WHEN a request fails with a non-JSON response
        THEN it should raise a HeygenAPIError with the raw text content.
        """
        # ARRANGE
        error_text = "Internal Server Error"
        requests_mock.get(
            TEST_URL, status_code=HTTPStatus.INTERNAL_SERVER_ERROR, text=error_text
        )
        client = HeygenBaseClient()

        # ACT & ASSERT
        with pytest.raises(HeygenAPIError) as e:
            client.get(url=TEST_URL)

        assert e.value.status_code == HTTPStatus.INTERNAL_SERVER_ERROR
        assert e.value.message == error_text
