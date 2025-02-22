import json

import httpx

from .configs import CHAT_URL
from .utils import get_default_chat_payload, get_default_user_agent


class GrokClient:
    @property
    def headers(self):
        return {
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en-US,en;q=0.9",
            "Content-Type": "application/json",
            "Cookie": self.cookie,
            "Origin": "https://grok.com",
            "Referer": "https://grok.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": self.user_agent,
        }

    def __init__(self, cookie: str, user_agent: str | None = None):
        self.cookie = cookie
        self.user_agent = user_agent if user_agent else get_default_user_agent()
        self.client = httpx.AsyncClient()

    async def chat(self, prompt: str, model: str, reasoning: bool):
        default_payload = get_default_chat_payload()
        update_payload = {
            "modelName": model,
            "message": prompt,
            "isReasoning": reasoning,
        }
        default_payload.update(update_payload)
        payload = default_payload
        async with self.client.stream(
            method="POST",
            url=CHAT_URL,
            headers=self.headers,
            json=payload,
        ) as response:
            async for chunk in response.aiter_lines():

                chunk_json = json.loads(chunk)
                if "error" in chunk:
                    raise RuntimeError(chunk_json.get("error").get("message"))
                response = (
                    chunk_json.get("result", {}).get("response", {}).get("token", "")
                )
                yield response
