## Sieve of Eratosthenes to find all primes until a limit
def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False


N = 1000000
primes = list(primes_sieve2(N))
counters = [0 for i in xrange(N+1)]

## Fill the counters array with number of distinct factors
for prime in primes:
  for i in xrange(prime, N+1, prime):
    counters[i] += 1


four_distinct = map(lambda x: x == 4, counters)
for sub in xrange(3, N+1):
  if(all(four_distinct[sub-3:sub+1])):
    print "Found it", sub-3, "-", sub, ":)"
    exit(0)