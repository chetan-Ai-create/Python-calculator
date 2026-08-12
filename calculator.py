
try:
    a = int(input("enter a first number:"))

    b = int(input("enter a second number:"))

    print("what kind of operation do you want to perform")

    o = input("enter operation:")

    match o:
        case "+":
            print(f"the result is : {a + b}")
        case "-":
            print(f"the result is : {a - b}")
        case "*":
            print(f"the result is : {a * b}")
        case "/":
            print(f"the result is : {a / b}")

except Exception as e:
    print("enter a valid value")


