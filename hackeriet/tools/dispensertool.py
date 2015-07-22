#! /usr/bin/env python3

import hackeriet.user as user
import hackeriet.service.door
import hackeriet.service.ledger
import hackeriet.service.dispenser

def main():
    root = user.root('/tmp/user')
#    ledger = hackeriet.service.ledger.init(root)
#    door = hackeriet.service.door.init(root)
    disp = hackeriet.service.dispenser.init(root, '1234567890')

    print(list(disp.ledger.accounts))
    print(list(disp.ledger.transactions_since(0)))

#    print(list(ledger.accounts))
#    print(list(ledger.transactions_since(1433864810)))

    a = disp.ledger.account('brumle')
    a.deposit(10)
    a.deduct(9)
    print(a.balance)
#    s = dispenser.sync.Syncer(9000)
#    sys.stdin.read()

if __name__ == '__main__':
    main()
