

## Read and extract the words from the dictionary
with open('words.txt', 'r') as fin:
	lines = fin.read().split("\n")

## Create a set with the english words
english_words = frozenset(lines)

## Read the file
with open('cipher.txt', 'r') as fin:
	line = fin.readlines()[0]

## Ascii codes
codes = map(int, line.split(","))

## Chars
chars = map(chr, codes)

## Search al possible keys
max_words = -1
max_key = []
for i in xrange(97, 123):
	print i
	for j in xrange(97, 123):
		for k in xrange(97, 123):
			key = [i,j,k]
			replicated_key = [x for _ in xrange(len(chars)) for x in key]			
			
			zipped = zip(codes, replicated_key)
			decrypted = "".join([chr(x ^ y).lower() for x,y in zipped])
			
			real_words = 0
			for word in decrypted.split():
				if(word in english_words):
					real_words += 1	

			if(real_words > max_words):
				max_words = real_words
				max_key = key


print max_words
print max_key
replicated_key = [x for _ in xrange(len(chars)) for x in max_key]			

zipped = zip(codes, replicated_key)
decrypted = [chr(x ^ y) for x,y in zipped]

print decrypted
print "Sum of ascii codes: ", sum(map(ord, decrypted))