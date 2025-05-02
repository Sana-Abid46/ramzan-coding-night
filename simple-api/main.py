from fastapi import FastAPI
import random

app = FastAPI()


side_hustles = [
    "Freelance Web Development - Build websites using HTML, CSS, JavaScript, Django or Flask.",
    "Data Entry Automation - Automate repetitive tasks like Excel data entry with Python scripts.",
    "Resume & Portfolio Builder - Create and sell tools using Streamlit or Flask.",
    "Online Tutoring - Teach Python or web dev on Zoom, YouTube, or Preply.",
    "Social Media Automation - Use Selenium or Instabot to schedule posts or auto-reply DMs.",
    "Digital Islamic Library - Build apps to manage Islamic books using Streamlit.",
    "E-book Conversion Tool - Convert DOC/PDF to EPUB/Kindle using Python libraries.",
    "Blog Automation Tool - Post to WordPress/Blogger via Python APIs.",
    "Stock/Price Tracker - Monitor prices or stocks using BeautifulSoup or yfinance.",
    "PDF Invoice Generator - Generate invoices using fpdf2 or reportlab libraries."
]

money_quotes = [
    "1. Money is a terrible master but an excellent servant. – P.T. Barnum",
    "2. Do not save what is left after spending, but spend what is left after saving. – Warren Buffett",
    "3. It’s not your salary that makes you rich, it’s your spending habits. – Charles A. Jaffe",
    "4. A penny saved is a penny earned. – Benjamin Franklin",
    "5. The goal isn’t more money. The goal is living life on your terms. – Chris Brogan",
    "6. Too many people spend money they haven’t earned, to buy things they don’t want, to impress people they don’t like. – Will Rogers",
    "7. Time is more valuable than money. You can get more money, but you cannot get more time. – Jim Rohn",
    "8. Never depend on a single income. Make investments to create a second source. – Warren Buffett",
    "9. Formal education will make you a living; self-education will make you a fortune. – Jim Rohn",
    "10. The lack of money is the root of all evil. – Mark Twain"
]

@app.get("/side_hustles")
def get_side_hustles(apikey: str):
    """Return a random side hustle idea"""
    if apikey != "1234567890":
        return{"error": "invalid API key"}
    return {"side_hustle": random.choice(side_hustles)}


@app.get("/money_quotes")
def get_money_quotes(apikey:str):
    """Return a random money Quote"""
    if apikey != "1234567890":
        return{"error": "invalid API key"}
    return {"money_quote": random.choice(money_quotes)}
