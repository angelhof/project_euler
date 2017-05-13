from bisect import *

## Sieve of Eratosthenes to find all primes
def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False

primes = list(primes_sieve2(1000000))
primes_set = frozenset(primes)
odd_composites = (x for x in xrange(9,100000000,2) if x not in primes_set)
double_squares = [2 * (x ** 2) for x in range(100)]


for i in odd_composites:

  ## We have to check all primes below this maximum prime
  maximum_prime = bisect(primes, i)
  # print i, primes[maximum_prime]  

  flag = True
  for prim in primes[:maximum_prime][::-1]:
    for dsq in double_squares:
      if(dsq + prim > i):
        break
      elif(dsq + prim == i):
        flag = False
        break
    if(not flag):
      break
        

  if(flag):
    print "Found answer", i
    exit(0)