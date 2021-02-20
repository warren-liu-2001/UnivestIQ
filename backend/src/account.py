import math
import pandas as pd
from typing import List, Tuple, Dict
from findata import Security, Transaction

class Account:
    
    userid: int # UserID
    email: str #email
    password: str #password

    portfolio: List[Security] #stocks and equities held
    transactions: List[Transaction] #list of recent transactions: past 30 days
    spending_score: int # Unused spending score: may be used for ML


    def __init__(self, userid, email, password):
        self.userid = userid
        self.email = email
        self.password = password

    def setuserid(self, newid) -> None:
        self.userid = newid
    
    def getuserid(self) -> str:
        return self.userid

    def setemail(self, newem) -> None:
        self.email = newem
    
    def getemail(self) -> str:
        return self.email

    def setpwd(self, newpwd) -> None:
        self.password= newpwd
    
    def getpwd(self) -> str:
        return self.password

    def addsecurity(self, securityadd) -> None:
        self.portfolio.append(securityadd)
    
    def removesecurity(self, security_rm) -> bool:
        try:
            self.portfolio.remove(security_rm)
            return True
        except ValueError:
            return False
        except:
            return False
    
    def get_portfolio(self):
        listreturn = []
        for transaction in self.portfolio:
            listreturn.append(transaction)
        return listreturn

    def addtransaction(self, transacc) -> None:
        self.transactions.append(transacc)

    def removetransaction(self, transacc) -> None:
        try:
            self.transactions.remove(transacc)
            return True
        except ValueError:
            return False
        except:
            return False

    def get_transactions(self):
        listreturn = []
        for transaction in self.transactions:
            listreturn.append(transaction)
        return listreturn

    

