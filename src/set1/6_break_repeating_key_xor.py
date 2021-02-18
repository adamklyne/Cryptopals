#!/usr/bin/python3

a = 'this is a test'
b = 'wokka wokka!!!'
bin_a = []
bin_b = []

for i in range(len(a)):
    bin_a.append(format(ord(a[i]), 'b'))
    bin_b.append(format(ord(b[i]), 'b'))

def add_bits(a):
    for index, word in enumerate(a):
        if len(word)!=8:
            a[index] = '0'*(8-len(word)) + word
    return a

bin_a = add_bits(bin_a)
bin_b = add_bits(bin_b)

result = 0

for word in zip(bin_a, bin_b):
    for i in range(len(word[0])):
        if word[0][i]!=word[1][i]:
            result+=1

print(result)
