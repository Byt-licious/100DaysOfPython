def primechecker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print(f"The number is prime")
    else:
        print(f"The number is not prime")
n = int(input())    
primechecker(number = n)                
