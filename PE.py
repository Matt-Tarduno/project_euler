import math

################################################################################

def p1():
    '''
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
    '''
    sum=0
    for i in range(1000):
        if i%5==0 or i%3==0:
            sum+=i
    return(sum)

################################################################################

def p2():
    '''
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
    '''

################################################################################

def p3(n):
    while n%2==0:
        n=n//2
    i=3
    while i*i<n:
        if n%i==0:
            n=n//i
        else:
            i+=2
    #need to check for squares
    if n%int(math.sqrt(n))==0:
        n=int(math.sqrt(n))
    return n

################################################################################

def p4():
    '''
    A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    '''
    pal=0
    for i in range(1000,998001):
        if i%10==0:
            pass
        elif str(i)==str(i)[::-1]:
            #make sure number is product of two 3-digit numbers
            j=100
            while j<1000:
                if i%j==0 and 99<i/j<1000:
                    pal=i
                    break
                j+=1
    return pal

################################################################################


def p5():
    '''
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    '''
    #write numbers as dictionary of prime factorizations (after 10, numbers are redundant)
    prime_factorization_list=[{19:1},{2:1,3:2},{17:1},{2:4},{3:1,5:1},{2:1,7:1},{13:1},{2:2,3:1},{11:1},{2:1,5:1}]
    lcm={2:0,3:0,5:0,7:0,11:0,13:0,17:0,19:0}
    #edit dictionary including highest power of each prime factoe
    for number in prime_factorization_list:
        print(number)
        for factor in number:
            if number[factor]>lcm[factor]:
                lcm[factor]=number[factor]
    #multiply prime factors
    lcm_output=1
    for factor in lcm:
        lcm_output*=factor**lcm[factor]

    return lcm_output

################################################################################

def p6():
    '''
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 552 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    '''
    total=0
    for i in range(1,101):
        for j in range(1,101):
            if i!=j:
                total+=i*j
    return total

################################################################################

def p9():
    for a in range(1,1000):
        for b in range(a,1000):
            if (math.sqrt(a**2+b**2))%1==0.0 and a+b+int(math.sqrt(a**2+b**2))==1000:
                return (a*b*int(math.sqrt(a**2+b**2)))

################################################################################








