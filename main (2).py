year=int(input("enter year to be cheked:"))
if(year%4==0 and year%100!=0 or year%400==0):
 print(*"the yearisaleop year!")
else:
  print("the year isn't a leop")