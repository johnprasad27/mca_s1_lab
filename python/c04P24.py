class Bankccount:
  
    def __init__(self,customer_id,password,cash):
        self.customer_id=customer_id
        self.password=password
        self.cash=cash
        
    
    def deposit(self,customer_id,password):
        if customer_id == self.customer_id and password==self.password:
           cash=int(input("enter amount to deposit"))
           self.cash+=cash
           print(f"total cash",self.cash)

    def withdraw(self,customer_id,password):        
        if customer_id == self.customer_id and password==self.password:
           cash=int(input("enter amount to withdraw"))
           self.cash-=cash
           print(f"total cash",self.cash)
   
    def request_delete(self, customer_id, password):
        return (customer_id == self.customer_id and password == self.password)


accounts = {}

while True:
    print("\n BANK MENU")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Delete Account")
    print("5. Exit")

    choice = input("Enter the choice:")

    if choice=="1":
        cid = input("enter new customer id")
        if cid in accounts:
            print("duplicate customer id")
            continue
        pwd=input("enter password")
        cash=int(input("enter amount"))
        accounts[cid] = Bankccount(cid,pwd,cash)
        print("account successful")

    elif choice=="2":
          cid = input("enter new customer id")
          pwd = input("enter password")
          if cid in accounts:
              accounts[cid].deposit(cid,pwd)
          else:
              print("not possible")

    elif choice=="3":
          cid = input("enter new customer id")
          pwd = input("enter password")
          if cid in accounts:
              accounts[cid].withdraw(cid,pwd)
          else:
              print("not possible")

    elif choice=="4":
          cid = input("enter new customer id")
          pwd = input("enter password")
          if cid in accounts:
              if accounts[cid].request_delete(cid,pwd):
                  del accounts[cid]
          else:
              print("not possible")                        
    
    elif choice=="5":
        print("exiting")
        break
    else:
        print("invalid choice")