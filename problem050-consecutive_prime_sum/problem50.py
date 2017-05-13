import sys, os
sys.path.append('../lib') # or give the full path
from progress_bar import *

## Sieve of Eratosthenes to find all primes until a limit
def primes_sieve2(limit):
  a = [True] * limit                          # Initialize the primality list
  a[0] = a[1] = False

  for (i, isprime) in enumerate(a):
    if isprime:
      yield i
      for n in xrange(i*i, limit, i):     # Mark factors non-prime
        a[n] = False


N = 50000
primes = list(primes_sieve2(N))

primes_set = frozenset(primes_sieve2(1000000))
# print len(primes)
# print sum(primes[-21:])


consecutive = -1
summy_cons = -1


for leng in xrange(len(primes),0,-1):
  printProgressBar(len(primes) - leng, len(primes), prefix = 'Progress:', suffix = 'Complete', length = 50)
  # print leng, len(primes) - leng
  ## Test all consecutive sums with this length 
  for i in xrange(len(primes) - leng + 1):
    summy = sum(primes[i:i+leng])
    if(summy > 1000000):
      break
    elif(summy in primes_set):
      # print "Found it", summy, "with length", len(primes[i:i+leng])
      # print "Primes:", primes[i:i+leng]
      # exit(0)
      consecutive = leng
      summy_cons = summy

  if(consecutive > 0):
    printProgressBar(len(primes), len(primes), prefix = 'Progress:', suffix = 'Complete', length = 50)
    print "Found it:", summy_cons
    exit(0)
  