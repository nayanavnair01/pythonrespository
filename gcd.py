def gcd(n1,n2):
    if n1%n2==0:
        return n2
    return gcd(n2,n1%n2)
n1=int(input("enter 1st number:"))
n2=int(input("enter 2nd number"))
print(f"the gcd :{gcd(n1,n2)}")