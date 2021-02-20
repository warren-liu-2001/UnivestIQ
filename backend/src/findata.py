from typing import List, Tuple, Dict
from datetime import date, datetime

class Security:
    ticker: str # ticker of the security
    datebought: datetime #when it was "bought"
    buyprice: float #price it was "bought" at

    def __init__(self, ticker, date, price):
        self.buyprice = price
        self.ticker = ticker
        self.datebought = date

class Transaction:
    typeoftransact: str # ticker of the security
    explanation: str # what was this transaction about?
    dateoccur: datetime #when it was "occurred"
    amount: float #amount within this transaction

    def __init__(self, identity, explanation, dateoccur, amount):
        self.dateoccur = dateoccur
        self.typeoftransact = identity
        self.explanation = explanation
        self.amount = amount