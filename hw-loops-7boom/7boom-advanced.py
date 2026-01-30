num=int(input("Enter num!"))
for Z in range(100):
    ones=num % 10
    if ones==7:
        print("Boom")
        break
    num=num//10
    if num ==0:
        break 

     

