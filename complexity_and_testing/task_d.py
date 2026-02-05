a = int(input())
b = int(input())
c = int(input())

if c < 0:
    print("NO SOLUTION")

elif a == 0:
    if b == c ** 2:
        print("MANY SOLUTION")
    else:
        print("NO SOLUTION")
    
else:
    x = (c ** 2 - b) / a
    if x.is_integer():
        if (a * x + b) < 0:
            print("NO SOLUTION")
        else:
            print(int(x))
    else:
        print("NO SOLUTION")