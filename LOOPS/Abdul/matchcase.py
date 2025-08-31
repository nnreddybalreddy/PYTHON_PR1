dayNo=int(input("Enter a day number"))

if dayNo == 0:
    print("Monday")
elif dayNo == 1:
    print("Tuesday")
elif dayNo == 2:
    print("Wednesday")
elif dayNo == 3:
    print("Thrusday")
elif dayNo == 4:
    print("Friday")
elif dayNo == 5:
    print("Saturday")
elif dayNo == 6:
    print("Sunday")
else:
    print("Invalid day")

day = 4
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")                     