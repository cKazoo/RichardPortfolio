
print("Hello World!")
num1 = input("Enter First Value: ")
num2 = input("Enter Second Value: ")

num1 = int(num1)
num2 = int(num2)
operation = input("What operation do you wish to run? (A,S,M,D)")
print(num1)
print(num2)
print(operation)
if operation == "M":
    print(str(num1*num2))
elif operation == "A":
    print(str(num1+num2))
elif operation == "S":
    print(str(num1-num2))
elif operation == "D":
    print(str(num1/num2))
else:
    print("Operation failure, make sure value provided is an integer and operation letter is CAPATALIZED")