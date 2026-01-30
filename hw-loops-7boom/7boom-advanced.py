import sys

num = int(input("Enter num!"))

# If number is divisible by 7 (and not zero), print Boom immediately and exit.
if num != 0 and num % 7 == 0:
    print("Boom")
    sys.exit()

# Otherwise scan digits; print Boom once if any digit is 7, then exit.
for i in range(100):  # upper bound protects against unexpected large loops
    ones = num % 10
    if ones == 7:
        print("Boom")
        sys.exit()
    num //= 10
    if num == 0:
        break

