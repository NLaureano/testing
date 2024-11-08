import pytest
from bank import Account

def test_initial_balance():
    account = Account("NICK", 100)
    assert(100 == account.getbalance())

def test_deposit():
    account = Account("NICK", 100)
    account.deposit(100)
    assert(200 == account.getbalance())
    

def test_withdraw():
    account = Account("NICK", 100)
    account.withdraw(100)
    assert(0 == Nick.getbalance())
