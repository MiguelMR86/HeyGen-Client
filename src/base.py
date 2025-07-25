import json
import logging
from typing import Optional

import requests

import settings.api as api
from error_handlers import heygen_request_error_handler

logger = logging.getLogger(__name__)


class HeygenBaseClient:
    def __init__(self):
        self._session = requests.Session()
        self.api_urls = api.API_URLS

    def _get_headers(self) -> dict:
        return {
            "Authorization": f"Bearer {api.API_KEY}",
            "Content-Type": "application/json",
        }

    @heygen_request_error_handler
    def post(self, *, url: str, payload: Optional[dict] = None) -> requests.Response:
        # logger.debug(f"Payload: {json.dumps(payload, indent=2, default=str)}")
        response = self._session.post(url, json=payload, headers=self._get_headers())

        response.raise_for_status()
        return response

    @heygen_request_error_handler
    def get(self, *, url: str, params: Optional[dict] = None) -> requests.Response:
        # logger.debug(f"Params: {json.dumps(params, indent=2, default=str)}")
        response = self._session.get(url, params=params, headers=self._get_headers())

        response.raise_for_status()
        return response
