number = int(input("Enter a two-digit number: "))

tens = number // 10   
ones = number % 10      

print("  The sum of the digits is:", tens + ones)
print(ones * 10 + tens)
print()

number = int(input("Enter a three-digit number: "))

hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10

print("The sum of the digits is:", hundreds + tens + ones)
print(ones * 100 + tens * 10 + hundreds)
print(ones,tens,hundreds)
