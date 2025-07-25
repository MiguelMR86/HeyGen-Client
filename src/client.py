from base import HeygenBaseClient
from clients.avatar import AvatarClient
from clients.translator import TranslatorClient
from clients.video import VideoClient
from clients.voice import VoiceClient


class HeyGenClient:
    """
    Aggregator client to interact with all HeyGen API endpoints.
    Provides access to avatar, video, voice, and translator clients.
    """

    def __init__(self):
        client = HeygenBaseClient()
        self.video = VideoClient(client)
        self.avatar = AvatarClient(client)
        self.voice = VoiceClient(client)
        self.translator = TranslatorClient(client)
