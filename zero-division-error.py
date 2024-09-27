x=int(input())
y=int(input())
try:
    result=x/y
except ZeroDivisionError:
    print("zeroderror")
else:  
 print(result)

