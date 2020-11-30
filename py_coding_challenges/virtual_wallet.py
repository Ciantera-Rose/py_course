import os
import random

class Atm:
  def __init__(self):
    pass

  def transaction(self):
    self.trans_num = random.randint(100000000, 999999999)
    print(f"Transaction Confirmation: #{self.trans_num}")
    return self.trans_num

  def check_balance(self):
    global avl_bal  
    print(f"Available Balance: ${avl_bal}") 
    return avl_bal

  def deposit(self):
    global avl_bal
    dep_money = float(input('Please enter deposit amount: '))
    print(f"Money deposited: ${dep_money}")  
    i = int(input(f"Please confirm deposit amount of ${dep_money}:\n 1: Yes \n 2: No\n\nENTER: "))
    if i == 1:
      if dep_money > 0 and dep_money <= 1000:
         avl_bal += dep_money
         print(f"Deposit Successful")
         print(f"Available Balance: ${avl_bal}")
         return avl_bal
         #Exception for anything above 5000
      elif dep_money > 1000:
        print('Exceeds maximum deposit amount of $1000.\nPlease visit finanical institution or deposit new amount.')   
      else:
         print(f"You have exceeded the maximun deposit amount of $1000 \n Please try again ") 
    else:
         print(f"Available Balance: ${avl_bal}")
         print(f"Please select from the main menu to begin")
    return avl_bal    
    
  def withdraw(self):
    global avl_bal
    withdraw = float(input(f"Available Balance: ${avl_bal}\nEnter amount to withdraw: \n"))
    i = int(input(f"Please confirm withdrawal amount of ${withdraw}:\n 1: Yes \n 2: No\n\nENTER: "))
    if i == 1:
      if withdraw > 0 and withdraw <= avl_bal: 
        print(f"Retrive your cash withdrawl of ${withdraw}")
        avl_bal -= withdraw
        print(f"\nAvailable Balance: ${avl_bal}")
      elif withdraw > 1000:
        print(f"Exceeds maximum withdraw amount of $500.")
      elif withdraw > avl_bal:
         print(f"Insufficient funds")
         print(f"Available Balance: ${avl_bal}")
         return avl_bal
    else:  
      print(f"Available Balance: ${avl_bal}")
      print(f"Thank you for being a valued customer.")
      print(f"Please select from the main menu to begin.")
    return avl_bal


avl_bal = 800
obj = Atm()
bank_session = True
while bank_session:
  print("\n\nGALATIC BANK\n\nWelcome Valued Customer!\nSelect an option to continue: \n")
  i = int(input(" 1: CHECK BALANCE \n 2: DEPOSIT MONEY \n 3: WITHDRAW \n 4: EXIT \n\n ENTER: "))
  os.system('clear')
  if i == 1:
    obj.check_balance()
    obj.transaction()
  elif i == 2:
    obj.deposit()
    obj.transaction()
  elif i == 3:
    obj.withdraw()
    obj.transaction()
  elif i == 4:
    print(f"Thank you for being a valued customer!\nPlease take your card.")
  else:
    print("Please select a valid option from the menu")
         


    





