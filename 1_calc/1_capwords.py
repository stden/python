import string
s = 'The quick brown fox jumped over the lazy dog.'
print (s) 
print (string.capwords(s))
# The Quick Brown Fox Jumped Over The Lazy Dog.

leet = string.maketrans('abegiloprstz', '463611092572')
print (s.translate(leet))