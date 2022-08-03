
#Primality check using Fermat's Little theorem
#-----------------------------------------------------------

p = int(input("enter a number: "))
# a should be given in such a way that a is positive and not divisible by p.
a = int(input("enter the value of a: "))
if p > 1:
    b = a**(p-1)
    if b % p == 1:
        print(p,"is prime")
    else:
        print("not prime")
elif p ==1 or p ==0:
    print(p,"is not prime")

