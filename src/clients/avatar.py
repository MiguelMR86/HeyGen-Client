from base import HeygenBaseClient


class AvatarClient:
    """
    Client to interact with HeyGen API for avatar operations.
    """

    def __init__(self, client: HeygenBaseClient):
        self._client = client

    def list_all(self):
        """
        List all avatars.
        """
        url = f"{self._client.api_urls['v2']}/avatars"
        return self._client.get(url=url)
