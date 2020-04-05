while True:
 input_value = input("Please enter a number ")
 try:
  if int(input_value) % 1 != 0:
    print("Wrong input")
  elif int(input_value) % 2 == 0:
    print("True")
  else:
    print("False")
  break;
 except ValueError:
    print("This is not a number. Please enter a valid number")