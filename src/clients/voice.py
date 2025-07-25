from base import HeygenBaseClient


class VoiceClient:
    """
    Client to interact with HeyGen API for voice operations.
    """

    def __init__(self, client: HeygenBaseClient):
        self._client = client

    def list_all(self):
        """
        List all voices.
        """
        url = f"{self._client.api_urls['v2']}/voices"
        response = self._client.get(url=url).json()
        data = response.get("data", None)
        voices = data.get("voices", [])
        return voices
