import pytest

from dto.avatar import HeyGenAvatar
from dto.video import (
    HeyGenBackgroundColor,
    HeyGenBackgroundImage,
    HeyGenBackgroundVideo,
    HeyGenVideoDimension,
    HeyGenVideoInput,
)
from dto.voice import HeyGenTextVoice
from settings.video import (
    HEYGEN_DEFAULT_VIDEO_BACKGROUND_COLOR,
    HEYGEN_DEFAULT_VIDEO_HEIGHT,
    HEYGEN_DEFAULT_VIDEO_WIDTH,
)


class TestHeyGenVideoDimension:
    def test_default_values(self):
        video_dimension = HeyGenVideoDimension()
        assert video_dimension.width == HEYGEN_DEFAULT_VIDEO_WIDTH
        assert video_dimension.height == HEYGEN_DEFAULT_VIDEO_HEIGHT

    def test_to_dict(self):
        video_dimension = HeyGenVideoDimension()
        assert video_dimension.to_dict() == {
            "width": HEYGEN_DEFAULT_VIDEO_WIDTH,
            "height": HEYGEN_DEFAULT_VIDEO_HEIGHT,
        }


class TestHeyGenBackgroundColor:
    def test_default_values(self):
        background_color = HeyGenBackgroundColor()
        assert background_color.value == HEYGEN_DEFAULT_VIDEO_BACKGROUND_COLOR

    def test_to_dict(self):
        background_color = HeyGenBackgroundColor()
        assert background_color.to_dict() == {
            "type": "color",
            "value": HEYGEN_DEFAULT_VIDEO_BACKGROUND_COLOR,
        }


class TestHeyGenBackgroundImage:

    def test_to_dict(self):
        background_image = HeyGenBackgroundImage(
            image_asset_id="123",
        )
        assert background_image.to_dict() == {
            "type": "image",
            "image_asset_id": "123",
        }

        background_image = HeyGenBackgroundImage(
            url="https://example.com/image.png",
        )
        assert background_image.to_dict() == {
            "type": "image",
            "url": "https://example.com/image.png",
        }

    def test_to_dict_with_image_asset_id(self):
        background_image = HeyGenBackgroundImage(
            image_asset_id="123",
        )
        assert background_image.to_dict() == {
            "type": "image",
            "image_asset_id": "123",
        }

    def test_to_dict_with_url(self):
        background_image = HeyGenBackgroundImage(
            url="https://example.com/image.png",
        )
        assert background_image.to_dict() == {
            "type": "image",
            "url": "https://example.com/image.png",
        }

    def test_assert_image_asset_id_and_url(self):
        with pytest.raises(AssertionError):
            HeyGenBackgroundImage(
                image_asset_id="123",
                url="https://example.com/image.png",
            )

    def test_assert_image_asset_id_or_url(self):
        with pytest.raises(AssertionError):
            HeyGenBackgroundImage()


class TestHeyGenVideoInput:
    def test_to_dict(self):
        video_input = HeyGenVideoInput(
            character=HeyGenAvatar(
                avatar_id="123",
            ),
            voice=HeyGenTextVoice(
                voice_id="123",
                input_text="Hello, world!",
            ),
            background=HeyGenBackgroundColor(
                value="#000000",
            ),
        )

        assert video_input.to_dict().keys() == {
            "character",
            "voice",
            "background",
        }
