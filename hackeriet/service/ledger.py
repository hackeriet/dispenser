import os
from hackeriet import Archiver

class Ledger(object):
    def __init__(self, userdb, dispenser_id):
        self.__userdb = userdb
        self.__dispenser_id = dispenser_id
        self.__accounts = {}
    @property
    def accounts(self):
        return (self.account(user.name) for user in self.__userdb.all())
    def account(self, name):
        if name in self.__accounts:
            return self.__accounts[name]
        a = Account(self.__userdb.user(name), self.__dispenser_id)
        self.__accounts[name] = a
        return a
    def transactions_since(self, timestamp):
        for a in self.accounts:
            yield (a.name, list(a.transactions_since(timestamp)))

class Transaction(object):
    def __init__(self, hash, when, amount):
        self.__hash = hash
        self.__amount = amount
        self.__when = when
    def save_to(self, basedir):
        path = os.path.join(basedir, self.__hash)
        with open(path, "w") as ous:
            ous.write("%d %d" % (self.__when, self.__amount))
    def timestamp(self):
        return self.__when
    def __repr__(self):
        return "Transaction(hash=%s, amount=%d, when=%d)" % (self.__hash, self.__amount, self.__when)

class Account(object):
    def __init__(self, user, dispenser_id):
        self.__user = user
        self.__history = []
        self.__balance = 0
        self.__writedir = os.path.join('account', 'dispenser', dispenser_id)
        self.__basedir = os.path.join('account', 'dispenser')
        if user.path_exists(self.__basedir):
            self.__load()
        else:
            user.ensure_dir(self.__basedir)
        user.ensure_dir(self.__writedir)
    @property
    def name(self):
        return self.__user.name
    def __load(self):
        u = self.__user
        for f in u.listdir(self.__basedir):
            dirpath = os.path.join(self.__basedir, f)
            for g in u.listdir(dirpath):
                path = os.path.join(dirpath, g)
                with open(u.fullpath(path), "r") as ins:
                    hash = f
                    line = ins.readlines()[0]
                    [when, amount] = line.split(" ")
                    when = int(when)
                    amount = int(amount)
                    tx = Transaction(hash, when, amount)
                    self.__history.append(tx)
                    self.__balance += amount
    def deduct(self, amount):
        tx = Transaction(uuid.uuid1().hex, int(time.time()), -amount)
        tx.save_to(u.fullpath(self.__writedir))
        self.__history.append(tx)
        self.__balance -= amount
    def deposit(self, amount):
        tx = Transaction(uuid.uuid1().hex, int(time.time()), amount)
        tx.save_to(u.fullpath(self.__writedir))
        self.__history.append(tx)
        self.__balance += amount
    def __repr__(self):
        return "Account(name=%s, balance=%d, #tx=%d)" % (self.__user.name, self.__balance, len(self.__history))
    def transactions_since(self, timestamp):
        return (x for x in self.__history if x.timestamp() >= timestamp)

def init(root, dispenser_id):
    return Ledger(Archiver(root), dispenser_id)

