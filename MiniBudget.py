class Budget:

  def __init__(self,category,budget):
    self.category = category
    self.budget = budget
    self.table = []

  def exp(self, amount, description="N/A"):
    if self.budget>=amount:
      amount = -abs(amount)
      self.budget = self.budget + amount
      b = round(self.budget,2)
      self.table.append({amount, description})
      print("You have £" + str(b) + " left")
      return self.table
    else:
      print("Not enough money")


jan_f=Budget("food", 35) 
jan_f.exp(amount=20) # adding expenses without giving description
thing = jan_f.exp(10,"lunch with John") #adding expenses adding a description

import pandas as pd # importing pandas
df = pd.DataFrame(thing, columns=["amount", "description"])
print(df)
print(df["description"].sum())
df["description_times_two"] = df["description"]*2
df["description power of two"] = df["description"].apply(lambda x: x**2)
print(df)

starting_amount = float(input("Enter your starting amount: £"))
exp=[]
print("Enter your expenses and type Done when finished")
while True:
  expenses=input("Enter your expenses: ")
  if expenses=="Done":
    break
  number=float(expenses)
  exp.append(number)
you_spent = sum(exp)
remaining = starting_amount - you_spent

print("You started with £" + str(starting_amount))
print("You spent £" + str(you_spent))
print("Remaining £" + str(remaining))

if remaining > 0:
  print ("You were £" + str(remaining) + "underbudget")
else:
  print ("You overspend £" + str(abs(remaining)))

