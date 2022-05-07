import threading
import asyncio
import httpx
import json

class QuoteScraper:
    def __init__(self):
        self.base_url      = "https://free-quotes-api.herokuapp.com/"
        self.quotes_file   = "quotes.txt"
    
    async def get_quote(self):
        async with httpx.AsyncClient() as client:
            while True:
                    
                response = await client.get(self.base_url)

                quote = json.loads(response.text)['quote']
                
                with open(self.quotes_file, "a", encoding="utf-8") as handler:
                    handler.write(f"{quote}\n")
                    print('\u001b[36;1m[\u001b[0m~\u001b[36;1m] \u001b[0m Quote   • ', quote)
                    await asyncio.sleep(0.00009)

async def run():
    tasks = []
    for _ in range(248):
        tasks.append(QuoteScraper().get_quote())
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(run())
