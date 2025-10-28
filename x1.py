#Function for prime
def prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#Twin prime and Input
N=int(input("Enter:"))

for i in range(1,N,2):
    a=prime(i)
    b=prime(i+2)
    if a and b:
        print(i,i+2)
