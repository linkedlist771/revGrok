import asyncio

from revgrok import GrokClient


async def main():
    cookie = "Your cookie here"  # put your cookie here
    model = "grok-3"
    prompt = "9.8 and 9.11 which is bigger?"
    client = GrokClient(cookie=cookie)
    async for response in client.chat(prompt=prompt, model=model, reasoning=False):
        print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
