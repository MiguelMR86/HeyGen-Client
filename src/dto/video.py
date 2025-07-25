from dataclasses import dataclass, field
from typing import Optional

from dto.avatar import HeyGenAvatar
from dto.voice import HeyGenSilenceVoice, HeyGenTextVoice
from settings.video import (
    HEYGEN_DEFAULT_VIDEO_BACKGROUND_COLOR,
    HEYGEN_DEFAULT_VIDEO_HEIGHT,
    HEYGEN_DEFAULT_VIDEO_WIDTH,
)


@dataclass
class HeyGenVideoDimension:
    width: int = HEYGEN_DEFAULT_VIDEO_WIDTH
    height: int = HEYGEN_DEFAULT_VIDEO_HEIGHT

    def to_dict(self):
        return {
            "width": self.width,
            "height": self.height,
        }


@dataclass
class HeyGenBackgroundColor:
    value: str = HEYGEN_DEFAULT_VIDEO_BACKGROUND_COLOR

    def to_dict(self):
        return {
            "type": "color",
            "value": self.value,
        }


@dataclass
class HeyGenBackgroundImage:
    image_asset_id: Optional[str] = None
    url: Optional[str] = None

    def __init__(self, image_asset_id: Optional[str] = None, url: Optional[str] = None):
        assert image_asset_id or url, "image_asset_id or url must be provided"
        assert not (
            image_asset_id and url
        ), "image_asset_id and url cannot be provided together"

        self.image_asset_id = image_asset_id
        self.url = url

    def to_dict(self):
        if self.image_asset_id:
            return {
                "type": "image",
                "image_asset_id": self.image_asset_id,
            }
        elif self.url:
            return {
                "type": "image",
                "url": self.url,
            }


@dataclass
class HeyGenBackgroundVideo:
    asset_id: str

    def to_dict(self):
        return {
            "type": "video",
            "video_asset_id": self.asset_id,
            "play_style": "loop",
        }


@dataclass
class HeyGenVideoInput:
    character: HeyGenAvatar
    voice: HeyGenTextVoice | HeyGenSilenceVoice
    background: (
        HeyGenBackgroundColor | HeyGenBackgroundImage | HeyGenBackgroundVideo
    ) = field(default_factory=HeyGenBackgroundColor)

    def to_dict(self):
        return {
            "character": self.character.to_dict(),
            "voice": self.voice.to_dict(),
            "background": self.background.to_dict(),
        }
