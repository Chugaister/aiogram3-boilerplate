from typing import Any, Dict

import aiohttp

from utils.getenv import config

from .exceptions import exception_factory


class ApiClient:

    def __init__(self, base_url: str):
        self.base_url = base_url

    async def get(self, endpoint: str, headers: dict[str: str] = None) -> Dict[str, Any]:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(f"{self.base_url}{endpoint}") as response:
                if response.status <= 300:
                    return await response.json()
                else:
                    raise exception_factory(response.status, await response.json())

    async def post(self, endpoint: str, data: Dict[str, Any], headers: dict[str: str] = None) -> Dict[str, Any]:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(f"{self.base_url}{endpoint}", json=data) as response:
                if response.status <= 300:
                    return await response.json()
                else:
                    raise exception_factory(response.status, await response.json())

    async def delete(self, endpoint: str, headers: dict[str: str] = None) -> Dict[str, Any]:
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.delete(f"{self.base_url}{endpoint}") as response:
                if response.status <= 300:
                    return await response.json()
                else:
                    raise exception_factory(response.status, await response.json())


api_client = ApiClient(config.API_URL)
