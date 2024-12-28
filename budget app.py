class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = list()
    
  def __str__(self):
    title = f'{self.name:*^30}\n'
    items = ''
    total = 0

    for item in self.ledger:
      items += f"{item['description'][0:23]:23}" + f"{item['amount']:>7.2f}" + '\n'
      total += item['amount']
    
    output = title + items + 'Total: ' + str(total)
    return output
  
  def deposit(self, amount, description=''):
    '''Accepts an amount and description. If no description is given, it should default to an empty string. The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.'''
    self.ledger.append({"amount": amount, "description": description})

  def withdraw(self, amount, description = ''):
    '''Amount passed in should be stored in the ledger as a negative number. If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.'''
    if self.check_funds(amount):
      self.ledger.append({"amount": -amount, "description": description})
      return True
    return False
      
  def get_balance(self):
    '''Returns the current balance of the budget category based on the deposits and withdrawals that have occurred.'''
    total = 0
    for items in self.ledger:
      total += items['amount']
    return total

  def transfer(self, amount, category):
    '''Accepts an amount and another budget category as arguments. The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.'''
    if self.check_funds(amount):
      self.withdraw(amount, 'Transfer to ' + category.name)
      category.deposit(amount, 'Transfer from ' + self.name)
      return True
    return False

  def check_funds(self, amount):
    '''Accepts an amount as an argument. It returns False if the amount is greater than the balance of the budget category and returns True otherwise. This method should be used by both the withdraw method and transfer method.'''
    if amount <= self.get_balance():
      return True
    return False

def create_spend_chart(categories):
  output = 'Percentage spent by category\n'

  spent_dict = {}
  for i in categories:
    s = 0 
    for j in i.ledger:
      if j['amount'] < 0 :
        s+= abs(j['amount'])
    spent_dict[i.name] = round(s,2)
  total = sum(spent_dict.values())
  
  percent_dict = {}
  for k in spent_dict.keys():
    percent_dict[k] = int(round(spent_dict[k]/total,2)*100)
  for i in range(100,-10,-10):
    output += f'{i}'.rjust(3) + '| '
    for percent in percent_dict.values():
      if percent >= i:
        output+= 'o  '
      else:
        output+= '   '
    output += '\n' 
    
  output += ' '*4 + '-'*(len(percent_dict.values())*3+1)
  output += '\n     '
  
  dict_key_list = list(percent_dict.keys())
  max_len_category = max([len(i) for i in dict_key_list])
  
  for i in range(max_len_category):
    for name in dict_key_list:
      if len(name)>i:
        output+= name[i] +'  '
      else:
        output+= '   '
    if i < max_len_category-1:
      output+='\n     '
    
  return output
