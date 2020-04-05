input_value = input("Please enter your data ")
try:
 if type(input_value) == int:
         print ("True")

 elif type(int(input_value)) == int:
      print("True")
 elif type(input_value)!= int or type(input_value) != str or type(ord(input_value)) != int:
     print("False")
 else:
     print ("False")
except ValueError:
    print("str or not possible to parse as an int")