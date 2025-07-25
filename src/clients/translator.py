from base import HeygenBaseClient


class TranslatorClient:
    """
    Client to interact with HeyGen Translator API.
    """

    def __init__(self, client: HeygenBaseClient):
        self._client = client

    def list_languages(self):
        """
        List all languages.
        """
        url = f"{self._client.api_urls['v2']}/video_translate/target_languages"
        return self._client.get(url=url)

    def translate(self, video_url: str, output_language: str, title: str):
        """
        Translate text to target language.
        """
        url = f"{self._client.api_urls['v2']}/video_translate"
        return self._client.post(
            url=url,
            payload={
                "video_url": video_url,
                "output_language": output_language,
                "title": title,
            },
        )
