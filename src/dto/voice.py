from dataclasses import dataclass, field
from typing import Literal

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


@dataclass
class HeyGenElevenLabsSettings:
    model: Literal[
        "eleven_monolingual_v1",
        "eleven_multilingual_v1",
        "eleven_multilingual_v2",
        "eleven_turbo_v2",
        "eleven_turbo_v2_5",
    ] = HEYGEN_DEFAULT_ELEVEN_LABS_MODEL
    similarity_boost: float = HEYGEN_DEFAULT_ELEVEN_LABS_SIMILARITY_BOOST
    stability: float = HEYGEN_DEFAULT_ELEVEN_LABS_STABILITY
    style: float = HEYGEN_DEFAULT_ELEVEN_LABS_STYLE

    def to_dict(self) -> dict:
        return {
            "model": self.model,
            "similarity_boost": self.similarity_boost,
            "stability": self.stability,
            "style": self.style,
        }


@dataclass
class HeyGenTextVoice:
    input_text: str
    voice_id: str
    speed: float = HEYGEN_DEFAULT_TEXT_VOICE_SPEED
    emotion: str = HEYGEN_DEFAULT_TEXT_VOICE_EMOTION
    locale: str = HEYGEN_DEFAULT_TEXT_VOICE_LOCALE
    type: Literal["text"] = HEYGEN_DEFAULT_TEXT_VOICE_TYPE
    elevenlabs_settings: HeyGenElevenLabsSettings = field(
        default_factory=HeyGenElevenLabsSettings
    )

    def to_dict(self) -> dict:
        return {
            "type": self.type,
            "input_text": self.input_text,
            "voice_id": self.voice_id,
            "speed": self.speed,
            "emotion": self.emotion,
            "locale": self.locale,
            "elevenlabs_settings": self.elevenlabs_settings.to_dict(),
        }


@dataclass
class HeyGenSilenceVoice:
    duration: float
    type: Literal["silence"] = HEYGEN_DEFAULT_SILENCE_VOICE_TYPE

    def to_dict(self):
        return {"type": self.type, "duration": self.duration}
