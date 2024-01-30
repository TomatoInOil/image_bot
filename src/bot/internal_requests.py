import logging
import urllib.parse

from httpx import AsyncClient, Response

from bot.logger import log_start_and_end

API_URL = "http://127.0.0.1:8000/api/v1/"

_LOGGER = logging.getLogger(__name__)


class APIService:
    def __init__(self, base_url):
        self.base_url = base_url

    @log_start_and_end(logger=_LOGGER)
    async def save_photo(self, photo_bytearray: bytearray, filename: str, file_id: str):
        endpoint_urn = "photos/"
        files = dict(photo=(filename, bytes(photo_bytearray), "image/jpeg"))
        data = dict(file_id=file_id)
        await self.post_request(endpoint_urn, files, data)

    @log_start_and_end(logger=_LOGGER)
    async def post_request(self, endpoint_urn, files, data):
        async with AsyncClient() as client:
            url = urllib.parse.urljoin(base=self.base_url, url=endpoint_urn)
            response: Response = await client.post(url=url, files=files, data=data)
            response.raise_for_status()
