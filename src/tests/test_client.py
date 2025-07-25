from client import HeyGenClient
from clients.avatar import AvatarClient
from clients.translator import TranslatorClient
from clients.video import VideoClient
from clients.voice import VoiceClient


def test_heygen_client_initialization():
    """
    GIVEN a HeyGenClient instance is created
    WHEN its attributes are accessed
    THEN it should have correctly initialized all the specific clients.
    """
    client = HeyGenClient()

    assert isinstance(client.video, VideoClient)
    assert isinstance(client.avatar, AvatarClient)
    assert isinstance(client.voice, VoiceClient)
    assert isinstance(client.translator, TranslatorClient)

    # Also assert they share the same underlying base client instance
    assert client.video._client is client.avatar._client
    assert client.avatar._client is client.voice._client
    assert client.voice._client is client.translator._client
