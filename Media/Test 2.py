# cook your dish here
t=int(input())
for tc in range(t):
    sal=int(input())
    if (sal<1500):
        gs=float(sal+(0.1*sal)+(0.9*sal))
    elif (sal>1500):
        gs=float(sal+500+(0.98*sal))
    print (gs)
