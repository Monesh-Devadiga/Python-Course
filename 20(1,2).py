"""
#20.1 Banking System Simulation 
class Account:
    def __init__(self, id, hname):
        self.id = id
        self.hname = hname
        self._bal = 0 #encapsulation

    def checkbal(self):
        print(f"balance is {self._bal}")
    def deposit(self, amt):
        self._bal += amt
        print(f"Deposit success. Updated bal is {self._bal}")
    def withdraw(self, amt):
            if self._bal >= amt:
                 self._bal -= amt
                 print(f"Withdraw success. Updated bal is {self._bal}")
            else:
                print(f"Withdraw Failed bal is {self._bal}")

class savingsacc(Account):
     
     def calint(self):
          intrrate = 0.04
          intr = self._bal * intrrate
          print(f"Interest: {intr}")

class currentacc(Account):
    def withdraw(self, amt):
                 overlimit = 1000
                 if self._bal + overlimit >= amt:
                      self._bal -= amt
                      print(f"Withdraw success. Updated bal is {self._bal}")
                 else:
                     print(f"Ask is over limit")

class Bank:
    def __init__(self, name, city):
          self.name = name
          self.city = city
          self.__accounts = {}

    def createacc(self, id, hname, type):
        if type == "savings":
                newacc = savingsacc(id, hname)
        elif type == "current":
            newacc = currentacc(id, hname)
        self.__accounts[id] = newacc
        print("Account creation is successful")
        return newacc

    def getacc(self, id):
        if id not in self.__accounts:
            print("Acc not found")
            return None
        else:
            acc = self.__accounts[id]
            print(f"\nAccount ID is: {acc.id}\n Holder name is:{acc.hname}")
            return acc

b1 = Bank("Canara", "Bhatkal")

print("For Savings Account")
sav1 = b1.createacc("1", "Monesh", "savings")
sav1.deposit(int(input("Enter Amount to be deposit: ")))
sav1.withdraw(int(input("Enter Amount to be Withdraw: ")))
print("Total interest is:")
sav1.calint()
print("\n")
print("For Current Account")
cur1 = b1.createacc("2", "Krishna", "current")
cur1.deposit(int(input("Enter Amount to be deposit: ")))
cur1.withdraw(int(input("Enter Amount to be Withdraw: ")))
"""

#=====================================================================================
#20.2  Students Report Generation

class student:
    def __init__(self, rno, name):
        self.rno = rno
        self.name = name
        self.__marks = {}

    def addmarks(self, sub, marks):
        self.__marks[sub] = marks

    def calavg(self):
        total = 0
        for marks in self.__marks.items():
            total += marks
        avg = total/len(self.__marks)
        print(f"{self.name}'s Average {avg}")

    def ispassed(self):
        haspassed = any(marks < 35 for marks in self.__marks.values())
        if haspassed:
            print(f"{self.name} has passed")
        else:
            print(f"{self.name} has failed")

    def calgrade(self):
        per = self.calavg()*100
        if per >= 95:
            print("A+")
        elif per >= 90 and per < 95:
            print("A")
        elif per >= 85 and per < 90:
            print("Distinction")
        elif per >= 80 and per < 85:
            print("B")
        elif per >= 40 and per < 80:
            print("Passed")
        else:
            print("Failed")

a = student(1, "Monesh")
a.addmarks("Maths", 95)
a.addmarks("Science", 85)



    

