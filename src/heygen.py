import argparse
import csv
import json
import logging
import sys
from logging import getLogger

from client import HeyGenClient
from dto.avatar import HeyGenAvatar
from dto.video import HeyGenVideoInput
from dto.voice import HeyGenTextVoice
from exceptions import HeygenAPIError
from log_config import setup_logging

logger = getLogger(__name__)


class HeyGenClientManager:

    def __init__(self):
        self.client = HeyGenClient()
        self.parser = argparse.ArgumentParser(
            description="A command-line interface for the HeyGen API."
        )
        self.subparsers = self.parser.add_subparsers(
            dest="action", help="Available actions", required=True
        )
        self._setup_parsers()

    def _setup_parsers(self):
        """
        Sets up subparsers for each available action.
        """
        self.subparsers.add_parser("list_voices", help="List all available voices.")

        parser_generate = self.subparsers.add_parser(
            "generate_video", help="Generate a video from a CSV file."
        )
        parser_generate.add_argument(
            "csv_file",
            type=str,
            help="Path to the CSV file. Must contain 'text', 'avatar_id', and 'voice_id' columns.",
        )
        parser_generate.add_argument(
            "--title",
            type=str,
            default="Generated Video",
            help="The title of the video.",
        )

        self.subparsers.add_parser("list_avatars", help="List all available avatars.")

        self.subparsers.add_parser("list_videos", help="List all available videos.")

    def run(self):
        """
        Parses arguments and executes the corresponding action.
        """
        args_list = [arg for arg in sys.argv[1:]]
        args = self.parser.parse_args(args_list)

        action_method_name = f"action__{args.action}"
        action_method = getattr(self, action_method_name, None)

        if action_method:
            action_method(args)
        else:
            logger.error(f"Unknown action '{args.action}'")
            self.parser.print_help()
            sys.exit(1)

    def action__list_voices(self):
        """
        Lists all available voices from the HeyGen API.
        """
        response = self.client.voice.list_all()
        logger.info(json.dumps(response, indent=2, default=str))

    def action__list_avatars(self):
        """
        Lists all available avatars from the HeyGen API.
        """
        response = self.client.avatar.list_all()
        logger.info(json.dumps(response, indent=2, default=str))

    def action__list_videos(self):
        """
        Lists all available videos from the HeyGen API.
        """
        response = self.client.video.list_all()
        logger.info(json.dumps(response, indent=2, default=str))


def main():
    """
    Main function to run the HeyGen client manager.
    """
    # Set log level based on --debug flag
    log_level = logging.DEBUG if "--debug" in sys.argv else logging.INFO
    setup_logging(level=log_level)

    manager = HeyGenClientManager()
    manager.run()


if __name__ == "__main__":
    main()
