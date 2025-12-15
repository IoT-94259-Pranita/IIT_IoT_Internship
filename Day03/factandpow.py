n=int(input("enter number="))
base=int(input("enter base="))
exp=int(input("enter exp="))

def fact(n):
    if n==0 or n==1:
        return 1
    return n*fact(n-1)

def power(base,exp):
    if exp==0:
        return 1
    return base*power(base,exp-1)

print("factorail=",fact(n))
print("Power=",power(base,exp))
      