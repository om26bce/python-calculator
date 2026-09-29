def add():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=a+b
    print("The sum of",a,"and",b,"is:",c)
    
def diff():
    a=int(input("Enter first number: "))
    b=int(input("Enter number to be subtracted: "))
    c=a-b
    print("The difference of",a,"and",b,"is:",c)
    
def multi():
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))
    c=a*b
    print("The product of",a,"and",b,"is:",c)
    
def div():
    a=int(input("Enter first number: "))
    b=int(input("Enter number to be divided by: "))
    if b==0:
        print("Error: Division by zero is not allowed.")
    else:   
        c=a/b
        print("The division of",a,"by",b,"is:",c)
    
def powerr():
    a=int(input("Enter first number: "))
    b=int(input("Enter exponent: "))
    c=a**b
    print("The result of",a,"raised to the power of",b,"is:",c)
    
def modulus():
    a = int(input("Enter number to be divided: "))
    b = int(input("Enter divisor: "))
    if b == 0:
        print("Error: Division by zero is not allowed.")
    else:
        c = a % b
        print("The remainder of", a, "divided by", b, "is:", c)
    
def factorial():
    a = int(input("Enter a number: "))
    if a < 0:
        print("Factorial is not defined for negative numbers")
    else:
        result = 1
        for i in range(1, a + 1):
            result *= i
        print("The factorial of", a, "is:", result)
        
def percentage():
    part = float(input("Enter the part value: "))
    whole = float(input("Enter the whole value: "))
    if whole == 0:
        print("Cannot calculate percentage with a whole value of 0")
    else:
        result = (part / whole) * 100
        print(part, "is", result, "% of", whole)
        
        
def gcd_lcm():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    x, y = a, b
    while y:
        x, y = y, x % y
    gcd = x
    lcm = abs(a * b) // gcd if gcd != 0 else 0
    print("GCD of", a, "and", b, "is:", gcd)
    print("LCM of", a, "and", b, "is:", lcm)
    

def dataconversion(x,y):
    if x=="1": 
        original=int(input("Enter decimal number: "))
        if y=="1":
            print("Decimal to Decimal:",original)
        elif y=="2":
            c=str(bin(original))
            print("Decimal to Binary:",c[2:])
        elif y=="3":
            c=str(oct(original))
            print("Decimal to Octal:",c[2:])
        elif y=="4":
            c=str(hex(original))
            print("Decimal to Hexadecimal:",c[2:])
    elif x == "2":
        original = input("Enter binary number: ")
        decimal_value = int(original, 2)
        if y == "1":
            print("Binary to Decimal:", decimal_value)
        elif y == "2":
            print("Binary to Binary:", original)
        elif y == "3":
            c = str(oct(decimal_value))
            print("Binary to Octal:", c[2:])
        elif y == "4":
            c = str(hex(decimal_value))
            print("Binary to Hexadecimal:", c[2:])

    elif x == "3":
        original = input("Enter octal number: ")
        decimal_value = int(original, 8)
        if y == "1":
            print("Octal to Decimal:", decimal_value)
        elif y == "2":
            c = str(bin(decimal_value))
            print("Octal to Binary:", c[2:])
        elif y == "3":
            print("Octal to Octal:", original)
        elif y == "4":
            c = str(hex(decimal_value))
            print("Octal to Hexadecimal:", c[2:])

    elif x == "4":
        original = input("Enter hexadecimal number: ")
        decimal_value = int(original, 16)
        if y == "1":
            print("Hexadecimal to Decimal:", decimal_value)
        elif y == "2":
            c = str(bin(decimal_value))
            print("Hexadecimal to Binary:", c[2:])
        elif y == "3":
            c = str(oct(decimal_value))
            print("Hexadecimal to Octal:", c[2:])
        elif y == "4":
            print("Hexadecimal to Hexadecimal:", original)
            

def average():
    n = int(input("How many numbers do you want to average? "))
    if n <= 0:
        print("Please enter a positive number of values.")
        return
    numbers = []
    for i in range(n):
        num = float(input(f"Enter number {i + 1}: "))
        numbers.append(num)
    result = sum(numbers) / n
    print("The average of", numbers, "is:", result)
            
print("Welcome to the calculator program!")
        
ans="yes"
while "yes" in ans.lower():
    print("Select operation.")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Power")
    print("6.Data Conversion")
    print("7.Modulus")
    print("8 factorial")
    print("9.Percentage")
    print("10.GCD and LCM")
    print("11.Average")

    choice=input("Enter choice(1/2/3/4/5/6/7/8/9/10/11): ")

    if choice=="1":
        add()
    elif choice=="2":
        diff()
    elif choice=="3":
        multi()
    elif choice=="4":
        div()
    elif choice=="5":
        powerr()
    elif choice=="6":
        print("Select data type of original value:")
        print("1.Decimal")
        print("2.Binary")
        print("3.Octal")
        print("4.Hexadecimal")
        x=input("Enter choice(1/2/3/4): ")
        print("Select data type of converted value:")
        print("1.Decimal")
        print("2.Binary")
        print("3.Octal")
        print("4.Hexadecimal")
        y=input("Enter choice(1/2/3/4): ")
        dataconversion(x,y)
    elif choice=="7":
        modulus()
    elif choice=="8":
        factorial()
    elif choice=="9":
        percentage()
    elif choice=="10":
        gcd_lcm()
    elif choice=="11":
        average()
    else:
        print("Invalid input")
        
    ans=input("Do you want to continue? (yes/no): ")
