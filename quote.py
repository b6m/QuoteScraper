import threading
import asyncio
import httpx
import json

class QuoteScraper:
    def __init__(self):
        self.base_url      = "https://free-quotes-api.herokuapp.com/"
        self.quotes        = []
        self.blacklisted   = []
        self.duplicate     = []

    async def get_quote(self):
        async with httpx.AsyncClient() as client:
            while True:
                response = await client.get(self.base_url)
                quote = json.loads(response.text)["quote"]
                print(quote + "\n")
                with open("quotes.txt", "a") as f:
                    f.write(quote + "\n")
                    self.quotes.append(quote)
                blacklisted_chars = ['\ufffd']
                if any(char in quote for char in blacklisted_chars):
                    self.blacklisted.append(quote)
                    continue
                if quote in self.quotes:
                    self.duplicate.append(quote)
                    continue

async def run():
    tasks = []
    for _ in range(248):
        tasks.append(QuoteScraper().get_quote())
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(run())
