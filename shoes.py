x = int(input())
arr = list(map(int , input().split()))
print(arr)
c = int(input())
sum = 0
while(c > 0 and x > 0):
    y, z = input().split()
    if int(y) in arr:
        print("z",z)
        sum = sum + int(z)
        print("sum",sum)
        arr.remove(x)
        x = x - 1
    else:
        print("y not in arr")
    c = c - 1 
print(sum)
