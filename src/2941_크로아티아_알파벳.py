word = input()
word_len = len(word)
tmp = word.count('c=')
word_len -= tmp
tmp = word.count('c-')
word_len -= tmp
tmp = word.count('dz=')
word_len -= tmp * 2
tmp = word.count('d-')
word_len -= tmp
tmp = word.count('ij')
word_len -= tmp
tmp = word.count('nj')
word_len -= tmp
tmp = word.count('s=')
word_len -= tmp
tmp = word.count('z=')
word_len -= tmp
print(word_len)