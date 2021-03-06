import math
import uuid
from typing import Dict, List, Tuple
from datetime import date, datetime

import pandas as pd

from account import Account
from exceptionse import NotFoundError
from findata import Security, Transaction


class AccountManager:

    accounts: List[Account]

    def __init__(self):
        self.accounts = []

    def add_account(self, accounte: Account):
        self.accounts.append(accounte)

    def account_create(self, name: str, email: str, password: str):
        ident = uuid.uuid1().int
        acc = Account(ident, email, password, name)
        self.add_account(acc)

    def find_account(self, userid) -> Account:
        for account in self.accounts:
            if account.userid == userid:
                return account
        else:
            raise NotFoundError("Find account", "ERROR: Account Not found")

    def set_password(self, uuide, pwd) -> bool:
        try:
            acc = self.find_account(uuide)
            acc.setpwd(str(pwd))
            return True
        except NotFoundError:
            return False
        except:
            return False

    def authent_pwd(self, uuide, otherpwd, tries) -> bool:
        """
        IMPORTANT:
        the tries parameter takes an int and increments it. We have max of 5 tries until the logger is locked
        """
        try:
            acc = self.find_account(uuide)
            pwd = acc.getpwd
            if str(pwd) == str(otherpwd):
                return True
            else:
                tries += 1
                return False
        except NotFoundError:
            return False
        except:
            tries += 1
            return False

    def set_name(self, uuide, name):
        try:
            acc = self.find_account(uuide)
            acc.setname(str(name))
            return True
        except NotFoundError:
            return False
        except:
            return False

    def set_email(self, uuide, email):
        try:
            acc = self.find_account(uuide)
            acc.setemail(str(email))
            return True
        except NotFoundError:
            return False
        except:
            return False

    def get_uuid_from_email(self, email) -> int:
        for account in self.accounts:
            if account.email == email:
                return account.userid
        else:
            raise NotFoundError("Find UUID", "ERROR: UUID Not found from email")

    def add_investment(self, email, investment: Security) -> bool:
        try:
            uuide = self.get_uuid_from_email(email)
            acc = self.find_account(uuide)
            acc.addsecurity(investment)
            return True
        except NotFoundError:
            return False
        except:
            return False

    def remove_investment(self, email, investment: Security) -> bool:
        try:
            uuide = self.get_uuid_from_email(email)
            acc = self.find_account(uuide)
            acc.removesecurity(investment)
            return True
        except NotFoundError:
            return False
        except:
            return False

    def find_investment(self, investmentid) -> Security:
        for account in self.accounts:
            for investment in account.get_portfolio():
                if investment.id == investmentid:
                    return investment
        raise NotFoundError("Find Investment", "ERROR: Investment cannot be found")

    def remove_transaction(self, email, investment: Transaction) -> bool:
        try:
            uuide = self.get_uuid_from_email(email)
            acc = self.find_account(uuide)
            acc.removetransaction(investment)
            return True
        except NotFoundError:
            return False
        except:
            return False

    def add_transaction(self, email, investment: Transaction) -> bool:
        try:
            uuide = self.get_uuid_from_email(email)
            acc = self.find_account(uuide)
            acc.addtransaction(investment)
            return True
        except NotFoundError:
            return False
        except:
            return False

    def new_transaction(self, typeoftrs, explanation, amount) -> Transaction:
        datetimenow = datetime.now()
        uuuuid = uuid.uuid1().int
        return Transaction(uuuuid, typeoftrs, explanation, datetimenow, amount)


    def find_transaction(self, email, transactionID: int) -> Transaction:
        try:
            uuide = self.get_uuid_from_email(email)
            acc = self.find_account(uuide)
            transactions = acc.get_transactions
            for txn in transactions:
                if txn.ide == transactionID:
                    return txn
            else:
                return self.new_transaction("INVALID", "TXN NOT FOUND IN USER", 0)
        except NotFoundError:
            return self.new_transaction("INVALID", "NAN VALUE IN TXN", 0)
        except:
            return self.new_transaction("INVALID", "NAN VALUE IN TXN", 0)


