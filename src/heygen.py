import json
import logging
import os
import sys
from logging import getLogger

from colorlog import ColoredFormatter

from client import HeyGenClient
from exceptions import HeygenAPIError
from log_config import setup_logging

logger = getLogger(__name__)


class HeyGenClientManager:
    client = HeyGenClient()

    def handle_action(self, action: str | None, *args, **kwargs):
        try:
            function = getattr(self, f"action__{action}")
            function(*args, **kwargs)
        except AttributeError:
            logger.error(f"Action {action} not found\n")
            self.help()

    def action__list_voices(self):
        voices = self.client.voice.list_all()
        logger.debug(json.dumps(voices, indent=2, default=str))

    def action__list_avatars(self):
        avatars = self.client.avatar.list_all()
        logger.debug(json.dumps(avatars, indent=2, default=str))

    def action__list_videos(self):
        videos = self.client.video.list_all()
        print(videos)

    def action__generate_video(self):
        pass

    def help(self):
        actions = [
            func
            for func in dir(self)
            if func.startswith("action__") and not func.startswith("__")
        ]

        logger.info("Available actions:")
        for action in actions:
            logger.info(f"- {action.replace('action__', '')}")


def main():
    """
    Main function to run the HeyGen client manager.
    """
    setup_logging()
    manager = HeyGenClientManager()

    if len(sys.argv) < 2:
        logger.error("No action provided\n")
        manager.help()
    else:
        manager.handle_action(sys.argv[1], *sys.argv[2:])


if __name__ == "__main__":
    main()
