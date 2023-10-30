from colorama import Fore

print("What do you want to do?\n1 = Add\n2 = Subtract\n3 = Multiply\n4 = Divide")
expression = input("Option: ")
while True:
  if expression == "1":
    print("You are now adding some numbers! Please answer the following questions!")
    try:
      first_num = int(input("First Number: "))
      second_num = int(input("Second Number: "))
    except:
       print(Fore.RED + "1 or more of your numbers weren't valid!", Fore.WHITE)
    else:
      print("Your result is:", first_num + second_num)
      quit(0)
  elif expression == "2":
    print("You are now subtracting some numbers! Please answer the following questions!")
    try:
      first_num = int(input("First Number: "))
      second_num = int(input("Second Number: "))
    except:
       print(Fore.RED + "1 or more of your numbers weren't valid!", Fore.WHITE)
    else:
      print("Your result is:", first_num - second_num)
      quit(0)
  elif expression == "3":
    print("You are now multiplying some numbers! Please answer the following questions!")
    try:
      first_num = int(input("First Number: "))
      second_num = int(input("Second Number: "))
    except:
       print(Fore.RED + "1 or more of your numbers weren't valid!", Fore.WHITE)
    else:
      print("Your result is:", first_num * second_num)
      quit(0)
  elif expression == "4":
    print("You are now dividing some numbers! Please answer the following questions!")
    try:
      first_num = int(input("First Number: "))
      second_num = int(input("Second Number: "))
    except:
       print(Fore.RED + "1 or more of your numbers weren't valid!", Fore.WHITE)
    else:
      print("Your result is:", first_num / second_num)
      quit(0)
  else:
    print(Fore.RED + "You didn't enter a valid number!", Fore.WHITE)
    quit(0)
