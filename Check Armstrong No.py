n = int(input("Enter No: "))
sum = 0
tem = n
while tem > 0:
    dig = tem%10
    sum += dig**3
    tem //= 10

if n == sum:
    print("it is armstrong")
else:
    print("No")