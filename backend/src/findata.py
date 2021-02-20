from typing import List, Tuple, Dict
from datetime import date, datetime

class Security:
    id: int
    ticker: str # ticker of the security
    datebought: datetime #when it was "bought"
    buyprice: float #price it was "bought" at

    def __init__(self, id, ticker, datepr, price):
        self.id = id
        self.buyprice = price
        self.ticker = ticker
        self.datebought = datepr

    def __str__(self):
        return "Ticker: " + self.ticker + " Date Purchased: " + \
               self.datebought.__str__() + " Price: " + str(self.buyprice)


class Transaction:
    id: int
    typeoftransact: str # ticker of the transaction
    explanation: str # what was this transaction about?
    dateoccur: datetime #when it was "occurred"
    amount: float #amount within this transaction

    def __init__(self, identity, explanation, dateoccur, amount):
        self.dateoccur = dateoccur
        self.typeoftransact = identity
        self.explanation = explanation
        self.amount = amount

    def __str__(self):
        return "Date: " + self.dateoccur.__str__() + " Type: " + \
               self.typeoftransact + " Description: " + self.explanation + \
               " Amount: " + str(self.amount)

