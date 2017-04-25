from is_prime import is_prime

# Find all possible b values
bs = range(1,1001)

bs = filter(is_prime, bs)


max_prime = -1
max_p = -1
for a in range(-1000,1001):
  #print a
  for b in bs:
    curr = 0
    for n in xrange(10000000):
      res = n**2 + a*n + b      
      if(res > 0):      
        if(is_prime(res)):
          curr += 1
        else:
          break
      else:
        break
    if(curr > max_prime):
      max_prime = curr
      max_p = a * b

print "Max prime sequence:", max_prime
print "a*b", max_p
