from database import DBConn
from account import *
from findata import *
from manager import *
from recommender import *

class Access:
    curruser: Account
    am: AccountManager
    conn: DBConn
    recommender: Recommender

    def __init__(self):
        self.conn = DBConn()
        self.am = AccountManager()
        self.recommender = Recommender("ML Model", self.am)

    def loaddata(self):
        listacc = self.conn.export_user_data()
        for account in listacc:
            self.am.add_account(account)

    def savedata(self):
        listacc = self.am.accounts

        for account in listacc:
            self.conn.save_user_data(account.userid, account.name,
                                     account.password, account.email)

    tries = 0

    def logon(self, email, password) -> bool:

        uuid_user = self.am.get_uuid_from_email(email)
        authent = self.am.authent_pwd(uuid_user, password, tries)

        if tries > 3:
            self.curruser = None
            return False
        if authent == False:
            self.curruser = None
            tries += 1
            return False
        else:
            self.curruser = self.am.find_account(uuid_user)
            return True

    def return_efficientoutcome(self):
        if self.curruser != None:
            userdata = self.recommender.data_parse(self.curruser.userid)
            metadata = self.recommender.data_parse_general()
            userproc = self.recommender.data_process(userdata)
            metaproc = self.recommender.data_process(metadata)

            return self.recommender.tfML_Predict(metaproc, userproc)

        else:
            return ("NO OUTCOME", 0.0)



