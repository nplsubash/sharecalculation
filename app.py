from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from stock_calculator import StockCalculator
import logging
import os

# Configure logging
logging.basicConfig(
    filename="app.log",  # Log file
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("index.html", "r") as f:
        return HTMLResponse(content=f.read())

class Transaction(BaseModel):
    buy_price: float
    sell_price: float
    quantity: int
    brokerage_rate: float = 0.4
    capital_gains_tax: float = 5

@app.post("/calculate/")
async def calculate(transaction: Transaction):
    try:
        calculator = StockCalculator(
            buy_price=transaction.buy_price,
            sell_price=transaction.sell_price,
            quantity=transaction.quantity,
            brokerage_rate=transaction.brokerage_rate,
            capital_gains_tax=transaction.capital_gains_tax
        )
        report = calculator.generate_report()

        # Log the transaction
        logging.info(f"Transaction calculated: {report}")

        return report
    except Exception as e:
        logging.error(f"Error during calculation: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))