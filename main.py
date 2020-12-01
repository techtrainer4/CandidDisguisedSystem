def SplitTheBill():
  ppl = int(input("How many people?"))
  bill = float(input("How much was the bill?"))
  tip = float(input("How much is the tip?"))
  share = (1 + tip) * bill/ppl
  share = round(share,2)
  return share

age = 66
if age >= 65:
  print("You get a discount!")
elif age <= 5:
  print("You get in for free!")
elif age <= 18:
  print("You get a student discount.")
else:
  print("You pay full price.")

pizza = input("Do you like pizza?Write Yes or No.")

pizza = pizza.lower()

if pizza == "yes":
  print("I like pizza too!")
else:
  print("Why don't you like it?")



















