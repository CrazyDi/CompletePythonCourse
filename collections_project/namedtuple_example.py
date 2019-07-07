from collections import namedtuple

account = ('checking', 1850.90)

print(account[0])  # name
print(account[1])  # balance

Account = namedtuple('Account', ['name', 'balance'])

account = Account('checking', 1850.90)
print(account.name)
print(account)
