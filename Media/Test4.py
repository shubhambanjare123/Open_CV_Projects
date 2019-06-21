# cook your dish here
# cook your dish here
arr = input().split(' ')
x=arr[0]
y=arr[1]

if (x%5 != 0):
  print(y)
else:
    if ((x+0.5)<=y):
        print(y-(x+0.5))
    else:
        print(y)
    
    
