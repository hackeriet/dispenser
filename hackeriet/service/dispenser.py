from .ledger import Ledger

class Dispenser(object):
    def __init__(self, userdb, dispenser_id):
        self.__ledger = Ledger(userdb, dispenser_id)
    @property
    def ledger(self):
        return self.__ledger

def init(userdb, dispenser_id):
    return Dispenser(userdb, dispenser_id)
