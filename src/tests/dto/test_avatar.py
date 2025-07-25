from dto.avatar import HeyGenAvatar
from settings.avatar import (
    HEYGEN_DEFAULT_AVATAR_OFFSET_X,
    HEYGEN_DEFAULT_AVATAR_OFFSET_Y,
    HEYGEN_DEFAULT_AVATAR_SCALE,
    HEYGEN_DEFAULT_AVATAR_STYLE,
    HEYGEN_DEFAULT_AVATAR_TYPE,
)


class TestHeyGenAvatar:
    def test_default_values(self):
        avatar = HeyGenAvatar(
            avatar_id="123",
        )
        assert avatar.avatar_id == "123"
        assert avatar.avatar_style == HEYGEN_DEFAULT_AVATAR_STYLE
        assert avatar.type == HEYGEN_DEFAULT_AVATAR_TYPE
        assert avatar.scale == HEYGEN_DEFAULT_AVATAR_SCALE
        assert avatar.offset_x == HEYGEN_DEFAULT_AVATAR_OFFSET_X
        assert avatar.offset_y == HEYGEN_DEFAULT_AVATAR_OFFSET_Y

    def test_to_dict(self):
        avatar = HeyGenAvatar(
            avatar_id="123",
        )
        assert avatar.to_dict() == {
            "avatar_id": "123",
            "avatar_style": HEYGEN_DEFAULT_AVATAR_STYLE,
            "type": HEYGEN_DEFAULT_AVATAR_TYPE,
            "scale": HEYGEN_DEFAULT_AVATAR_SCALE,
            "offset": {
                "x": HEYGEN_DEFAULT_AVATAR_OFFSET_X,
                "y": HEYGEN_DEFAULT_AVATAR_OFFSET_Y,
            },
        }
