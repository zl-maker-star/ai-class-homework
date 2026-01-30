num = int(input("Enter num!"))

# Scan digits; print Boom once if any digit is 7.
for _ in range(100):  # upper bound protects against unexpected large loops
    ones = num % 10
    if ones == 7:
        print("Boom")
        break
    num //= 10
    if num == 0:
        break

