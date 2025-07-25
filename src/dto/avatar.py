from dataclasses import dataclass
from typing import Literal

from settings.avatar import (
    HEYGEN_DEFAULT_AVATAR_OFFSET_X,
    HEYGEN_DEFAULT_AVATAR_OFFSET_Y,
    HEYGEN_DEFAULT_AVATAR_SCALE,
    HEYGEN_DEFAULT_AVATAR_STYLE,
    HEYGEN_DEFAULT_AVATAR_TYPE,
)


@dataclass
class HeyGenAvatar:
    avatar_id: str
    avatar_style: Literal["normal"] = HEYGEN_DEFAULT_AVATAR_STYLE
    type: Literal["avatar"] = HEYGEN_DEFAULT_AVATAR_TYPE
    scale: float = HEYGEN_DEFAULT_AVATAR_SCALE
    offset_x: float = HEYGEN_DEFAULT_AVATAR_OFFSET_X
    offset_y: float = HEYGEN_DEFAULT_AVATAR_OFFSET_Y

    def to_dict(self):
        return {
            "avatar_id": self.avatar_id,
            "avatar_style": self.avatar_style,
            "type": self.type,
            "scale": self.scale,
            "offset": {
                "x": self.offset_x,
                "y": self.offset_y,
            },
        }
