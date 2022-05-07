import threading
import asyncio
import httpx
import json
import random

class QuoteScraper:
    def __init__(self):
        self.apis          = ["https://free-quotes-api.herokuapp.com/", "https://api.quotable.io/random"]
        self.quotes_file   = "quotes.txt"
    
    async def get_quote(self):
        async with httpx.AsyncClient() as client:
            while True:


                api = random.choice(self.apis)
                
                response = await client.get(api)
                
                data = json.loads(response.text)
                
                if "content" in data:
                    quote = data["content"]
                else:
                    quote = data["quote"]


                with open(self.quotes_file, "a", encoding="utf-8") as handler:
                    
                    
                    handler.write(f"{quote}\n")
                    
                    print(f'\u001b[36;1m[\u001b[0m~\u001b[36;1m] \u001b[0m {api} | Quote   • {quote}')
                    
                    await asyncio.sleep(0.00009)

async def run():
    tasks = []
    for _ in range(248):
        tasks.append(QuoteScraper().get_quote())
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(run())
