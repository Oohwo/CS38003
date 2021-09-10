# Robinhood is a famous stock trading platform in US.
# Create a class called Robinhood as follows:
# Each instance of the Robinhood class will hold the following information: name, record, and value
# The name is a string, which is the name of the owner.
# The record is a dictionary of stocks which the account owner has.
# For the record, the key is stock name , and the value is a list with three elements [market price, 
# avg price, quantity]. Market price is the current price of the stock, avg price is the average cost 
# of the stock, quantity is the shares you have.
# Value is a float number, which is the total amount of stocks you have.
#
# For example:
# I bought 5 shares Apple at $100. --->[100,100,5]
# I bought 5 shares Apple at $200. --->[200,150,10]
# Apple's price becomes $300 --->[300,150,10]
#
#
# Your task is to implement the following class methods:
# (1) __init__(self, name): the constructor creates a student instance with a given name.
# After initialization, the record is an empty dictionary and the value is 0.
# (2) get_name(self): returns the name of the owner
# (3) buy_stock(self, stock_name, market_price, quantity):  buy a stock, (stock_name, market_price, quantity),
# to owner's record. You need to update the record and vallue. If the stock is in the record, update the values of 
# record[stock_name]; if not, create a new key.
# (4) sell_stock(self, stock_name, market_price, quantity):  sell a stock, (stock_name, market_price, quantity),
# to owner's record. You need to update the record and value. Update the values of record[stock_name]. After the update, 
# if the quantity becomes zero, delete the key.
# (5) market(self, stock_name, market_price): Modify the market price of a stock in the record
# (6) get_record(self): returns the owner's stock record.
# (7) get_value(self): returns the value in the account.
#
# Example:
# >> rh = Robinhood('Alice')
# >> print(Robinhood.get_name())
# Alice
# >> print(Robinhood.get_value())
# 0
# >> rh.buy_stock('Apple', 100,5)
# >> print(rh.get_record())
# {'Apple': [100, 100, 5]}
# >> rh.buy_stock('Apple', 200,5)
# >> print(rh.get_record())
# {'Apple': [200, 150, 10]}
# (Hint: (100.0 * 5 + 200.0 * 5) / (5 + 5) = 150.0 )
# >> rh.market('Apple', 300)
# >> print(rh.get_record())
# {'Apple': [300, 150, 5]}
# >> print(rh.get_value())
# 1500
# (Hint: (300.0*5 = 1500.0))
# >> rh.sell_stock('Apple', 400,10)
# >> print(rh.get_record())

# TODO: Add comments
class Robinhood:
  def __init__(self, name):
    self.name = name
    self.record = {}
    self.value = 0

  def get_name(self):
    return self.name

  def buy_stock(self, stock_name, market_price, quantity):
    if stock_name in self.record:
      old_avg = self.record[stock_name][1]
      old_quant = self.record[stock_name][2]
      new_avg = ((old_avg * old_quant) + (market_price * quantity)) / (old_quant + quantity)
      self.record[stock_name] = [market_price, new_avg, old_quant + quantity]
    else:
      self.record[stock_name] = [market_price, (market_price * quantity) / quantity, quantity]
    
  def sell_stock(self, stock_name, market_price, quantity):
    old_avg = self.record[stock_name][1]
    old_quant = self.record[stock_name][2]
    if (old_quant - quantity == 0):
      del self.record[stock_name]
    else:
      self.record[stock_name] = [market_price, old_avg, old_quant - quantity]

  def market(self, stock_name, market_price):
    self.record[stock_name] = [market_price, self.record[stock_name][1],self.record[stock_name][2]]

  def get_record(self):
    return self.record

  def get_value(self):
    self.value = 0
    for stock_name in self.record:
      self.value = self.value + self.record[stock_name][0] * self.record[stock_name][2]
    return self.value

rh = Robinhood("Alice")
print(rh.get_name())
print(rh.get_value())

rh.buy_stock("Apple", 100, 5)
print(rh.get_record())
print(rh.get_value())
rh.buy_stock("Apple", 200, 5)
print(rh.get_record())
print(rh.get_value())
rh.market("Apple", 300)
print(rh.get_record())
print(rh.get_value())
