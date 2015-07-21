from .ledger import Ledger

"""
All dispenser data is stored in $user/accounts/dispenser/{dispenser_id}/
"""
class Dispenser(object):
    def __init__(self, userdb, dispenser_id):
        assert userdb
        assert dispenser_id
        self.__ledger = Ledger(userdb, dispenser_id)
    @property
    def ledger(self):
        return self.__ledger

"""
Initialize an instance of the Dispenser class. This method may eventually do memoization.

userdb -- an instance of UsersRoot
dispenser_id -- a unique id for this dispenser, as an id
"""
def init(userdb, dispenser_id):
    return Dispenser(userdb, dispenser_id)
