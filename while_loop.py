a = int(input("Enter a number: "))
rs = 0
while (a!=0):
    r = a%10
    rs = rs + r
    a = a//10
print("Reverse of the number is: ",rs) 