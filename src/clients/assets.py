from base import HeygenBaseClient


class AssetsClient:
    """
    Client to interact with HeyGen assets.
    """

    def __init__(self, client: HeygenBaseClient):
        self._client = client

    def upload(self, file_path: str):
        """
        Upload an asset.
        """
        with open(file_path, "rb") as file:
            url = f"{self._client.api_urls['v1']}/asset"
            return self._client.post(url=url, file=file)
