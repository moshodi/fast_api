from fastapi import FastAPI
from scraper import Scraper

app = FastAPI()

quotes = Scraper()

@app.get("/search")
async def read_item(cat: str):
    return quotes.scrapedata(cat)

@app.get('/')
def home():
    return 'hello world!'