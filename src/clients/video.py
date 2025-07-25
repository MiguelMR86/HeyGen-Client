import logging
import time

from base import HeygenBaseClient
from dto.video import HeyGenVideoDimension, HeyGenVideoInput

logger = logging.getLogger(__name__)


class VideoClient:
    """
    Client to interact with HeyGen API for video operations.
    """

    def __init__(self, client: HeygenBaseClient):
        self._client = client

    def list_all(self):
        """
        List all videos.
        """
        url = f"{self._client.api_urls['v1']}/video.list"
        return self._client.get(url=url)

    def generate(
        self,
        video_inputs: list[HeyGenVideoInput],
        title: str = "Generated Video",
        dimension: HeyGenVideoDimension = HeyGenVideoDimension(),
    ):
        """
        Generate a video from a script text.

        video_inputs: A list of video input objects.
        title: The title of the video.
        dimension: The dimension of the video.
        """
        url = f"{self._client.api_urls['v2']}/video/generate"

        payload = {
            "video_inputs": [input.to_dict() for input in video_inputs],
            "title": title,
            "dimension": dimension.to_dict(),
        }

        response = self._client.post(url=url, payload=payload)
        return response.json()

    def status(self, video_id: str):
        """
        Check the status of a video generation.

        video_id: The ID of the video returned by generate_video_from_script.
        The video file URL you get will expire in 7 days.
        """
        url = f"{self._client.api_urls['v1']}/video_status.get"
        params = {
            "video_id": video_id,
        }

        response = self._client.get(url=url, params=params)
        return response.json()

    def download(self, video_id: str):
        """
        Download a video from HeyGen.
        """

        status_url = f"{self._client.api_urls['v1']}/video_status.get"

        params = {
            "video_id": video_id,
        }

        while True:
            response = self._client.get(url=status_url, params=params)
            response_data = response.json()

            status = response_data["data"]["status"]

            if status == "completed":
                video_url = response_data["data"]["video_url"]
                thumbnail_url = response_data["data"]["thumbnail_url"]
                logger.info(
                    f"Video generation completed! \nVideo URL: {video_url} \nThumbnail URL: {thumbnail_url}"
                )

                # Save the video to a file
                video_filename = "generated_video.mp4"
                with open(video_filename, "wb") as video_file:
                    video_content_response = self._client.get(url=video_url)
                    video_content_response.raise_for_status()
                    video_file.write(video_content_response.content)
                break

            elif status == "processing" or status == "pending":
                logger.info("Video is still processing. Checking status...")
                time.sleep(5)

            elif status == "failed":
                error = response_data["data"]["error"]
                logger.error(f"Video generation failed. '{error}'")
                break
