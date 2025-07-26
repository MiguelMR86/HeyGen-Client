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
