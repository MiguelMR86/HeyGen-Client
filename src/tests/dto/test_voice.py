from dto.voice import HeyGenElevenLabsSettings, HeyGenSilenceVoice, HeyGenTextVoice
from settings.voice import (
    HEYGEN_DEFAULT_ELEVEN_LABS_MODEL,
    HEYGEN_DEFAULT_ELEVEN_LABS_SIMILARITY_BOOST,
    HEYGEN_DEFAULT_ELEVEN_LABS_STABILITY,
    HEYGEN_DEFAULT_ELEVEN_LABS_STYLE,
    HEYGEN_DEFAULT_SILENCE_VOICE_TYPE,
    HEYGEN_DEFAULT_TEXT_VOICE_EMOTION,
    HEYGEN_DEFAULT_TEXT_VOICE_LOCALE,
    HEYGEN_DEFAULT_TEXT_VOICE_SPEED,
    HEYGEN_DEFAULT_TEXT_VOICE_TYPE,
)


class TestHeyGenElevenLabsSettings:
    def test_default_values(self):
        eleven_labs_settings = HeyGenElevenLabsSettings()
        assert eleven_labs_settings.model == HEYGEN_DEFAULT_ELEVEN_LABS_MODEL
        assert (
            eleven_labs_settings.similarity_boost
            == HEYGEN_DEFAULT_ELEVEN_LABS_SIMILARITY_BOOST
        )
        assert eleven_labs_settings.stability == HEYGEN_DEFAULT_ELEVEN_LABS_STABILITY
        assert eleven_labs_settings.style == HEYGEN_DEFAULT_ELEVEN_LABS_STYLE

    def test_to_dict(self):
        eleven_labs_settings = HeyGenElevenLabsSettings()
        assert eleven_labs_settings.to_dict() == {
            "model": HEYGEN_DEFAULT_ELEVEN_LABS_MODEL,
            "similarity_boost": HEYGEN_DEFAULT_ELEVEN_LABS_SIMILARITY_BOOST,
            "stability": HEYGEN_DEFAULT_ELEVEN_LABS_STABILITY,
            "style": HEYGEN_DEFAULT_ELEVEN_LABS_STYLE,
        }


class TestHeyGenTextVoice:
    def test_default_values(self):
        text_voice = HeyGenTextVoice(
            input_text="Hello, world!",
            voice_id="123",
        )
        assert text_voice.speed == HEYGEN_DEFAULT_TEXT_VOICE_SPEED
        assert text_voice.emotion == HEYGEN_DEFAULT_TEXT_VOICE_EMOTION
        assert text_voice.locale == HEYGEN_DEFAULT_TEXT_VOICE_LOCALE
        assert text_voice.type == HEYGEN_DEFAULT_TEXT_VOICE_TYPE

    def test_to_dict(self):
        text_voice = HeyGenTextVoice(
            input_text="Hello, world!",
            voice_id="123",
        )
        text_voice_dict = text_voice.to_dict()
        assert text_voice_dict["type"] == HEYGEN_DEFAULT_TEXT_VOICE_TYPE
        assert text_voice_dict["input_text"] == "Hello, world!"
        assert text_voice_dict["voice_id"] == "123"
        assert text_voice_dict["speed"] == HEYGEN_DEFAULT_TEXT_VOICE_SPEED
        assert text_voice_dict["emotion"] == HEYGEN_DEFAULT_TEXT_VOICE_EMOTION
        assert text_voice_dict["locale"] == HEYGEN_DEFAULT_TEXT_VOICE_LOCALE


class TestHeygenElevenLabsSettings:
    def test_default_values(self):
        eleven_labs_settings = HeyGenElevenLabsSettings(
            model=HEYGEN_DEFAULT_ELEVEN_LABS_MODEL,
            similarity_boost=HEYGEN_DEFAULT_ELEVEN_LABS_SIMILARITY_BOOST,
            stability=HEYGEN_DEFAULT_ELEVEN_LABS_STABILITY,
            style=HEYGEN_DEFAULT_ELEVEN_LABS_STYLE,
        )
        assert eleven_labs_settings.model == HEYGEN_DEFAULT_ELEVEN_LABS_MODEL
        assert (
            eleven_labs_settings.similarity_boost
            == HEYGEN_DEFAULT_ELEVEN_LABS_SIMILARITY_BOOST
        )
        assert eleven_labs_settings.stability == HEYGEN_DEFAULT_ELEVEN_LABS_STABILITY
        assert eleven_labs_settings.style == HEYGEN_DEFAULT_ELEVEN_LABS_STYLE

    def test_to_dict(self):
        eleven_labs_settings = HeyGenElevenLabsSettings(
            model=HEYGEN_DEFAULT_ELEVEN_LABS_MODEL,
            similarity_boost=HEYGEN_DEFAULT_ELEVEN_LABS_SIMILARITY_BOOST,
            stability=HEYGEN_DEFAULT_ELEVEN_LABS_STABILITY,
            style=HEYGEN_DEFAULT_ELEVEN_LABS_STYLE,
        )
        assert eleven_labs_settings.to_dict() == {
            "model": HEYGEN_DEFAULT_ELEVEN_LABS_MODEL,
            "similarity_boost": HEYGEN_DEFAULT_ELEVEN_LABS_SIMILARITY_BOOST,
            "stability": HEYGEN_DEFAULT_ELEVEN_LABS_STABILITY,
            "style": HEYGEN_DEFAULT_ELEVEN_LABS_STYLE,
        }

    def test_to_dict_with_custom_values(self):
        eleven_labs_settings = HeyGenElevenLabsSettings(
            model="eleven_turbo_v2",
            similarity_boost=0.5,
            stability=0.4,
            style=0.6,
        )
        assert eleven_labs_settings.to_dict() == {
            "model": "eleven_turbo_v2",
            "similarity_boost": 0.5,
            "stability": 0.4,
            "style": 0.6,
        }


# WIP: TestHeyGenSilenceVoice
class TestHeyGenSilenceVoice:
    def test_default_values(self):
        silence_voice = HeyGenSilenceVoice(
            duration=1.0,
        )
        assert silence_voice.duration == 1.0
        assert silence_voice.type == HEYGEN_DEFAULT_SILENCE_VOICE_TYPE

    def test_to_dict(self):
        silence_voice = HeyGenSilenceVoice(
            duration=1.0,
        )
        assert silence_voice.to_dict() == {
            "type": HEYGEN_DEFAULT_SILENCE_VOICE_TYPE,
            "duration": 1.0,
        }
