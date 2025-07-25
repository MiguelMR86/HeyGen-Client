from unittest.mock import Mock

from clients.assets import AssetsClient


class TestAssetsClient:
    def test_upload(self):
        client = AssetsClient(client=Mock())
        assert client.upload("test.mp4") == "test.mp4"
