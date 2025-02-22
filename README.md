# revGrok: Unofficial Grok API Wrapper

revGrok is an unofficial implementation that allows you to interact with Grok’s API in reverse.

## Installation

To use this library, follow these simple steps:

1. Install the package:
   ```bash
   pip install -U revgrok
   ```

2. Obtain your authentication cookie:
   - Log in to the [Grok web app](https://grok.com) and start any conversation.
   - Record the cookie value from your browser.
   ![Cookie](assets/f8d26402-88b1-408c-9ec2-243b22b9ac85.png)

3. Use the library:
   A simple example script, [chat_example.py](chat_example.py), demonstrates how to interact with Grok.

### Example Usage

```python
import asyncio
from src.revgrok import GrokClient

async def main():
    cookie = "Your cookie here"  # Replace with your actual cookie
    model = "grok-3"  # Choose your model (e.g., grok-3)
    prompt = "9.8 and 9.11, which is bigger?"  # Define your prompt

    client = GrokClient(cookie=cookie)
    async for response in client.chat(prompt=prompt, model=model, reasoning=False):
        print(response, end="")

if __name__ == "__main__":
    asyncio.run(main())
```

- Set `reasoning=True` if you want to enable reasoning or leave it as `False` to disable it.
- For free accounts, your usage may soon be limited. Consider upgrading to a paid plan to avoid interruptions.

## Contribution

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request!
